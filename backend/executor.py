# ===============================================
# Python Code Executor
# -----------------------------------------------
# Description   : Safely executes Python code from files or strings,
#                 capturing stdout/stderr with timeout protection.
#                 Supports integration with parser.py for multilingual
#                 code translation and execution.
# Author(s)     : yashnarayan123, sproutcake23
# Created       : 2025-05-28
# Last Modified : 2025-09-24 17:30 (sproutcake23)
# Comment       : Executes Python code within a secure, isolated Docker container.
#                 This sandboxing approach prevents network access, file system
#                 modifications, and handles infinite loops via a timeout.
# Usage:
#     $ python executor.py -f script.py
#     $ python executor.py -c "print('Hello World')"
#     $ python executor.py --from-parser hindi demo/input_hindi.py
# ===============================================




import argparse
import os
import sys
import subprocess
import tempfile
from datetime import datetime
from contextlib import redirect_stdout, redirect_stderr

class PythonCodeExecutor:
    def __init__(self):
        """Initialize the executor with output directory setup."""
        self.output_dir = "execution_output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def execute_from_file(self, code_file_path: str) -> dict:
        """
        Execute Python code from a file.
        """
        if not os.path.isfile(code_file_path):
            raise FileNotFoundError(f"Code file not found: {code_file_path}")
        # Read the Python code from the file
        with open(code_file_path, 'r', encoding='utf-8') as f:
            python_code = f.read()
        return self.execute_code(python_code, os.path.basename(code_file_path))
    
    def execute_from_string(self, python_code: str, source_name: str = "direct_input") -> dict:
        """
        Execute Python code from a string.
        """
        return self.execute_code(python_code, source_name)
    
    def execute_code(self, python_code: str, source_name: str) -> dict:
        """
        Execute Python code and return results.
        """
        result = {
            'success': False,
            'stdout': '',
            'stderr': '',
            'execution_time': None,
            'output_file': None,
            'source_name': source_name
        }
        
        try:
            # Create temporary file with the code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp_file:
                temp_file.write(python_code)
                temp_file_path = temp_file.name
            
            # Record start time
            start_time = datetime.now()
            
            # Execute using subprocess for safety
            process = subprocess.run(
            [
                "docker", "run", "--rm",
                "--network", "none",
                "--storage-opt", "size=100m",
                "--memory", "256m",
                "--memory-swap", "256m",
                "-v", f"{temp_file_path}:/sandbox/code.py:ro",
                "convex-sandbox:latest",
                "/sandbox/code.py"
            ],
                capture_output=True,
                text=True,
                timeout=30,  # 30 second timeout
                encoding='utf-8'
            )
            
            # Record end time
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            # Store results
            result['success'] = process.returncode == 0
            result['stdout'] = process.stdout
            result['stderr'] = process.stderr
            result['execution_time'] = execution_time
            
            # Save output to file
            output_filename = self.generate_output_filename(source_name)
            result['output_file'] = self.save_execution_output(
                python_code, 
                result, 
                output_filename
            )
            
        except subprocess.TimeoutExpired:
            result['stderr'] = "⏰ Execution timed out (30 seconds limit)"
            result['execution_time'] = 30.0
        except Exception as e:
            result['stderr'] = f"💥 Execution error: {str(e)}"
            result['execution_time'] = 0.0
        
        return result
    
    def execute_with_parser_integration(self, lang: str, input_file: str) -> dict:
        """
        Run parser.py first, then execute the translated code.
        """
        try:
            # Run parser.py to get translated code
            parser_process = subprocess.run(
                [sys.executable, 'parser.py', '-l', lang, '-i', input_file],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if parser_process.returncode != 0:
                return {
                    'success': False,
                    'stdout': '',
                    'stderr': f"Parser failed: {parser_process.stderr}",
                    'execution_time': 0.0,
                    'output_file': None,
                    'source_name': input_file
                }
            
            # Extract translated code from parser output
            parser_output = parser_process.stdout
            if "✅ Translated Python Code:" in parser_output:
                # Extract code after the header
                code_start = parser_output.find("✅ Translated Python Code:") + len("✅ Translated Python Code:")
                translated_code = parser_output[code_start:].strip()
                
                # Remove any extra formatting
                if translated_code.startswith('\n'):
                    translated_code = translated_code[1:]
                
                # Execute the translated code
                return self.execute_code(translated_code, input_file)
            else:
                return {
                    'success': False,
                    'stdout': '',
                    'stderr': "Could not extract translated code from parser output",
                    'execution_time': 0.0,
                    'output_file': None,
                    'source_name': input_file
                }
                
        except Exception as e:
            return {
                'success': False,
                'stdout': '',
                'stderr': f"Integration error: {str(e)}",
                'execution_time': 0.0,
                'output_file': None,
                'source_name': input_file
            }
    
    def generate_output_filename(self, source_name: str) -> str:
        """Generate output filename based on source and timestamp."""
        base_name = os.path.splitext(source_name)[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_execution_{timestamp}.txt"
    
    def save_execution_output(self, python_code: str, result: dict, filename: str) -> str:
        """Save execution results to output file."""
        output_path = os.path.join(self.output_dir, filename)
        # Ensure any nested directories exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("🚀 PYTHON CODE EXECUTION RESULTS\n")
            f.write("=" * 70 + "\n")
            f.write(f"📅 Executed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"📁 Source: {result['source_name']}\n")
            f.write(f"⏱️  Execution time: {result['execution_time']:.4f} seconds\n")
            f.write(f"✅ Success: {'Yes' if result['success'] else 'No'}\n")
            f.write("\n")
            
            f.write("📝 EXECUTED PYTHON CODE:\n")
            f.write("-" * 40 + "\n")
            f.write(python_code + "\n\n")
            
            if result['stdout']:
                f.write("📄 PROGRAM OUTPUT:\n")
                f.write("-" * 40 + "\n")
                f.write(result['stdout'] + "\n\n")
            
            if result['stderr']:
                f.write("❌ ERROR OUTPUT:\n")
                f.write("-" * 40 + "\n")
                f.write(result['stderr'] + "\n\n")
            
            f.write("=" * 70 + "\n")
        
        return output_path


def main():
    """Main function for the executor."""
    parser = argparse.ArgumentParser(description="Execute Python code and save output results.")
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-f', '--file', type=str,
                           help='Python file to execute')
    input_group.add_argument('-c', '--code', type=str,
                           help='Python code string to execute')
    input_group.add_argument('--from-parser', nargs=2, metavar=('LANG', 'INPUT_FILE'),
                           help='Run parser first, then execute (e.g., --from-parser hindi demo/input_hindi.py)')
    
    # Output options
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Only save to file, minimal console output')
    parser.add_argument('--show-code', action='store_true',
                       help='Display the code before execution')
    
    args = parser.parse_args()
    
    executor = PythonCodeExecutor()
    
    try:
        # Determine execution method
        if args.file:
            if not args.quiet:
                print(f"📁 Executing Python file: {args.file}")
            result = executor.execute_from_file(args.file)
            
        elif args.code:
            if not args.quiet:
                print("📝 Executing Python code string...")
            if args.show_code:
                print("Code to execute:")
                print("-" * 30)
                print(args.code)
                print("-" * 30)
            result = executor.execute_from_string(args.code)
            
        elif args.from_parser:
            lang, input_file = args.from_parser
            if not args.quiet:
                print(f"🔄 Running parser for {lang} code, then executing...")
            result = executor.execute_with_parser_integration(lang, input_file)
        
        # Display results
        if result['success']:
            if not args.quiet:
                print(f"✅ Execution completed successfully!")
                print(f"⏱️  Time: {result['execution_time']:.4f} seconds")
                
                if result['stdout']:
                    print("\n📄 Program Output:")
                    print("-" * 40)
                    print(result['stdout'])
                    print("-" * 40)
            
            print(f"💾 Results saved to: {result['output_file']}")
            
        else:
            print("❌ Execution failed!")
            if result['stderr']:
                print(f"Error: {result['stderr']}")
            if result['output_file']:
                print(f"💾 Error details saved to: {result['output_file']}")
                
    except Exception as e:
        print(f"💥 Executor error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
