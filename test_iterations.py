"""
Pytest Test Suite for 0.3 Iterations Exercise
Tests student solutions for correctness and header completion
Run with: python -m pytest test_iterations.py -v
"""

import pytest
import sys
import io
from unittest.mock import patch
import importlib.util
import re
import os


# Path to student's file (in same directory)
STUDENT_FILE = '0.3_Iterations_Exercise.py'


def load_student_module():
    """Load the student's Python file as a module"""
    spec = importlib.util.spec_from_file_location("student_solution", STUDENT_FILE)
    module = importlib.util.module_from_spec(spec)
    return module, spec


def check_header_comments():
    """Check if student filled in author and date in header comments"""
    try:
        # Try UTF-8 first, then fall back to latin-1 which accepts all byte values
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        content = None
        
        for encoding in encodings:
            try:
                with open(STUDENT_FILE, 'r', encoding=encoding) as f:
                    lines = f.readlines()[:10]
                content = lines
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            # Last resort: read as binary and decode with errors='ignore'
            with open(STUDENT_FILE, 'rb') as f:
                raw = f.read()
            content = raw.decode('utf-8', errors='ignore').split('\n')[:10]
    
    except FileNotFoundError:
        return False, False, "File not found", "File not found"
    
    author_filled = False
    date_filled = False
    author_content = ""
    date_content = ""
    
    for line in content:
        if 'author:' in line.lower():
            parts = line.lower().split('author:', 1)
            if len(parts) > 1:
                content_part = parts[1].strip()
                if content_part and content_part != '':
                    author_filled = True
                    author_content = content_part
        if 'date:' in line.lower():
            parts = line.lower().split('date:', 1)
            if len(parts) > 1:
                content_part = parts[1].strip()
                if content_part and content_part != '':
                    date_filled = True
                    date_content = content_part
    
    return author_filled, date_filled, author_content, date_content


def extract_task_code(task_number):
    """Extract code for a specific task from the student file"""
    try:
        # Try multiple encodings
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        content = None
        
        for encoding in encodings:
            try:
                with open(STUDENT_FILE, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            # Last resort: binary read with error handling
            with open(STUDENT_FILE, 'rb') as f:
                raw = f.read()
            content = raw.decode('utf-8', errors='ignore')
    
    except FileNotFoundError:
        return ""
    
    # Split by task comments
    if task_number == 1:
        pattern = r'# Task 1:.*?(?=# Task 2a:|$)'
    elif task_number == '2a':
        pattern = r'# Task 2a:.*?(?=# 2b\)|$)'
    elif task_number == '2b':
        pattern = r'# 2b\).*?(?=# 2c\)|$)'
    elif task_number == '2c':
        pattern = r'# 2c\).*?(?=# 2d\)|$)'
    elif task_number == '2d':
        pattern = r'# 2d\).*?(?=# Task 3a\)|$)'
    elif task_number == '3a':
        pattern = r'# Task 3a\).*?(?=# 3b\)|$)'
    elif task_number == '3b':
        pattern = r'# 3b\).*?(?=# Task 4\)|$)'
    elif task_number == 4:
        pattern = r'# Task 4\).*?(?=# Task 5\)|$)'
    elif task_number == '5a':
        pattern = r'# Count the number of sevens.*?(?=# Count the number of odd digits|$)'
    elif task_number == '5b':
        pattern = r'# Count the number of odd digits.*?$'
    else:
        return ""
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        code = match.group(0)
        # Remove the comment line itself
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('#')])
        return code.strip()
    return ""


def run_task_code(task_code, inputs):
    """Run task code with mocked inputs and capture output"""
    output = io.StringIO()
    
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', output):
            try:
                exec(task_code, {'__name__': '__main__', 'random': __import__('random')})
            except StopIteration:
                pass  # Expected when inputs run out
            except Exception as e:
                return None, str(e)
    
    return output.getvalue(), None


def extract_numbers_from_output(output):
    """Extract all numbers from output string"""
    if output is None:
        return []
    numbers = re.findall(r'-?\d+\.?\d*', output)
    return [float(n) if '.' in n else int(n) for n in numbers]


# ==================== HEADER TESTS ====================

class TestHeaderComments:
    """Test that student filled in header comments"""
    
    def test_author_filled(self):
        """Check if author field is filled in"""
        author_filled, _, author_content, _ = check_header_comments()
        assert author_filled, f"Author field is empty or missing. Found: '{author_content}'"
    
    def test_date_filled(self):
        """Check if date field is filled in"""
        _, date_filled, _, date_content = check_header_comments()
        assert date_filled, f"Date field is empty or missing. Found: '{date_content}'"


# ==================== TASK 1 TESTS ====================

class TestTask1Factorial:
    """Test Task 1: Factorial calculation"""
    
    def test_factorial_5(self):
        """Test 5! = 120"""
        code = extract_task_code(1)
        if not code or len(code) < 10:
            pytest.skip("Task 1 code not found or incomplete")
        
        output, error = run_task_code(code, ['5'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 120 in numbers, f"Expected 120 in output, got: {output}"
    
    def test_factorial_0(self):
        """Test 0! = 1"""
        code = extract_task_code(1)
        if not code or len(code) < 10:
            pytest.skip("Task 1 code not found or incomplete")
        
        output, error = run_task_code(code, ['0'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 1 in numbers, f"Expected 1 in output (0! = 1), got: {output}"
    
    def test_factorial_7(self):
        """Test 7! = 5040"""
        code = extract_task_code(1)
        if not code or len(code) < 10:
            pytest.skip("Task 1 code not found or incomplete")
        
        output, error = run_task_code(code, ['7'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 5040 in numbers, f"Expected 5040 in output, got: {output}"


# ==================== TASK 2A TESTS ====================

class TestTask2aAverage:
    """Test Task 2a: Average of 5 marks"""
    
    def test_average_80_85_90_75_70(self):
        """Test average of 80, 85, 90, 75, 70 = 80.0"""
        code = extract_task_code('2a')
        if not code or len(code) < 10:
            pytest.skip("Task 2a code not found or incomplete")
        
        output, error = run_task_code(code, ['80', '85', '90', '75', '70'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        # Should have 80.0 or 80 in output
        assert 80.0 in numbers or 80 in numbers, f"Expected 80.0 in output, got: {output}"
    
    def test_average_all_100s(self):
        """Test average of all 100s = 100.0"""
        code = extract_task_code('2a')
        if not code or len(code) < 10:
            pytest.skip("Task 2a code not found or incomplete")
        
        output, error = run_task_code(code, ['100', '100', '100', '100', '100'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 100.0 in numbers or 100 in numbers, f"Expected 100.0 in output, got: {output}"


# ==================== TASK 2B TESTS ====================

class TestTask2bHighLow:
    """Test Task 2b: Average with high and low"""
    
    def test_high_low_80_85_90_75_70(self):
        """Test high=90, low=70, avg=80.0 for inputs 80,85,90,75,70"""
        code = extract_task_code('2b')
        if not code or len(code) < 10:
            pytest.skip("Task 2b code not found or incomplete")
        
        output, error = run_task_code(code, ['80', '85', '90', '75', '70'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 90 in numbers, f"Expected high=90 in output, got: {output}"
        assert 70 in numbers, f"Expected low=70 in output, got: {output}"
        assert 80.0 in numbers or 80 in numbers, f"Expected avg=80.0 in output, got: {output}"
    
    def test_extreme_values(self):
        """Test high=100, low=0, avg=50.0 for inputs 50,100,0,75,25"""
        code = extract_task_code('2b')
        if not code or len(code) < 10:
            pytest.skip("Task 2b code not found or incomplete")
        
        output, error = run_task_code(code, ['50', '100', '0', '75', '25'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 100 in numbers, f"Expected high=100 in output, got: {output}"
        assert 0 in numbers, f"Expected low=0 in output, got: {output}"
        assert 50.0 in numbers or 50 in numbers, f"Expected avg=50.0 in output, got: {output}"


# ==================== TASK 2C TESTS ====================

class TestTask2cValidation:
    """Test Task 2c: Input validation (0-100)"""
    
    def test_rejects_invalid_marks(self):
        """Test that invalid marks (150, -10) are rejected"""
        code = extract_task_code('2c')
        if not code or len(code) < 10:
            pytest.skip("Task 2c code not found or incomplete")
        
        # Inputs: 150 (invalid), -10 (invalid), then 5 valid marks
        output, error = run_task_code(code, ['150', '-10', '80', '85', '90', '75', '70'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        # Should still get avg=80, high=90, low=70 (from valid marks)
        assert 90 in numbers, f"Expected high=90 in output, got: {output}"
        assert 70 in numbers, f"Expected low=70 in output, got: {output}"
    
    def test_boundary_values_accepted(self):
        """Test that 0 and 100 are valid (boundary values)"""
        code = extract_task_code('2c')
        if not code or len(code) < 10:
            pytest.skip("Task 2c code not found or incomplete")
        
        output, error = run_task_code(code, ['0', '100', '50', '75', '25'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 100 in numbers, f"Expected high=100 in output, got: {output}"
        assert 0 in numbers, f"Expected low=0 in output, got: {output}"


# ==================== TASK 2D TESTS ====================

class TestTask2dSentinel:
    """Test Task 2d: Sentinel value (-1)"""
    
    def test_sentinel_stops_input(self):
        """Test that -1 stops input and calculates avg of 3 marks"""
        code = extract_task_code('2d')
        if not code or len(code) < 10:
            pytest.skip("Task 2d code not found or incomplete")
        
        output, error = run_task_code(code, ['80', '85', '90', '-1'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 85.0 in numbers or 85 in numbers, f"Expected avg=85.0 in output, got: {output}"
        assert 90 in numbers, f"Expected high=90 in output, got: {output}"
        assert 80 in numbers, f"Expected low=80 in output, got: {output}"


# ==================== TASK 3A TESTS ====================

class TestTask3aLargest:
    """Test Task 3a: Find largest positive integer"""
    
    def test_find_largest_30(self):
        """Test largest=30 from inputs 10,25,15,30,5,-1"""
        code = extract_task_code('3a')
        if not code or len(code) < 10:
            pytest.skip("Task 3a code not found or incomplete")
        
        output, error = run_task_code(code, ['10', '25', '15', '30', '5', '-1'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 30 in numbers, f"Expected largest=30 in output, got: {output}"
    
    def test_single_number(self):
        """Test with single input"""
        code = extract_task_code('3a')
        if not code or len(code) < 10:
            pytest.skip("Task 3a code not found or incomplete")
        
        output, error = run_task_code(code, ['5', '-1'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 5 in numbers, f"Expected largest=5 in output, got: {output}"


# ==================== TASK 3B TESTS ====================

class TestTask3bTwoLargest:
    """Test Task 3b: Find two largest integers"""
    
    def test_two_largest_30_25(self):
        """Test largest=30, second=25 from inputs 10,25,15,30,5,-1"""
        code = extract_task_code('3b')
        if not code or len(code) < 10:
            pytest.skip("Task 3b code not found or incomplete")
        
        output, error = run_task_code(code, ['10', '25', '15', '30', '5', '-1'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 30 in numbers, f"Expected largest=30 in output, got: {output}"
        assert 25 in numbers, f"Expected second largest=25 in output, got: {output}"
    
    def test_two_largest_200_175(self):
        """Test largest=200, second=175"""
        code = extract_task_code('3b')
        if not code or len(code) < 10:
            pytest.skip("Task 3b code not found or incomplete")
        
        output, error = run_task_code(code, ['100', '200', '50', '150', '175', '-1'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 200 in numbers, f"Expected largest=200 in output, got: {output}"
        assert 175 in numbers, f"Expected second largest=175 in output, got: {output}"


# ==================== TASK 4 TESTS ====================

class TestTask4Factors:
    """Test Task 4: Factor game"""
    
    def test_factors_of_12(self):
        """Test factors of 12 are 2,3,4,6"""
        code = extract_task_code(4)
        if not code or len(code) < 10:
            pytest.skip("Task 4 code not found or incomplete")
        
        # Mock random to always return 12
        import random
        with patch.object(random, 'randint', return_value=12):
            output, error = run_task_code(code, ['yes', 'no'])
            if error:
                pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        # Factors of 12 (excluding 1 and 12): 2, 3, 4, 6
        assert 2 in numbers, f"Expected factor 2 in output, got: {output}"
        assert 3 in numbers, f"Expected factor 3 in output, got: {output}"
        assert 4 in numbers, f"Expected factor 4 in output, got: {output}"
        assert 6 in numbers, f"Expected factor 6 in output, got: {output}"
    
    def test_factors_of_20(self):
        """Test factors of 20 are 2,4,5,10"""
        code = extract_task_code(4)
        if not code or len(code) < 10:
            pytest.skip("Task 4 code not found or incomplete")
        
        import random
        with patch.object(random, 'randint', return_value=20):
            output, error = run_task_code(code, ['yes', 'no'])
            if error:
                pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 2 in numbers, f"Expected factor 2 in output, got: {output}"
        assert 4 in numbers, f"Expected factor 4 in output, got: {output}"
        assert 5 in numbers, f"Expected factor 5 in output, got: {output}"
        assert 10 in numbers, f"Expected factor 10 in output, got: {output}"


# ==================== TASK 5A TESTS ====================

class TestTask5aSevens:
    """Test Task 5a: Count sevens in a number"""
    
    def test_count_sevens_in_7777(self):
        """Test counting 4 sevens in 7777"""
        code = extract_task_code('5a')
        if not code or len(code) < 10:
            pytest.skip("Task 5a code not found or incomplete")
        
        output, error = run_task_code(code, ['7777'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 4 in numbers, f"Expected 4 sevens in output, got: {output}"
    
    def test_count_sevens_in_1234567(self):
        """Test counting 1 seven in 1234567"""
        code = extract_task_code('5a')
        if not code or len(code) < 10:
            pytest.skip("Task 5a code not found or incomplete")
        
        output, error = run_task_code(code, ['1234567'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 1 in numbers, f"Expected 1 seven in output, got: {output}"
    
    def test_count_sevens_in_123456(self):
        """Test counting 0 sevens in 123456"""
        code = extract_task_code('5a')
        if not code or len(code) < 10:
            pytest.skip("Task 5a code not found or incomplete")
        
        output, error = run_task_code(code, ['123456'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 0 in numbers, f"Expected 0 sevens in output, got: {output}"


# ==================== TASK 5B TESTS ====================

class TestTask5bOddEven:
    """Test Task 5b: Count odd and even digits"""
    
    def test_count_odd_even_in_123456(self):
        """Test 3 odd (1,3,5) and 3 even (2,4,6) in 123456"""
        code = extract_task_code('5b')
        if not code or len(code) < 10:
            pytest.skip("Task 5b code not found or incomplete")
        
        output, error = run_task_code(code, ['123456'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 3 in numbers, f"Expected 3 odd and 3 even in output, got: {output}"
    
    def test_count_odd_even_in_2468(self):
        """Test 0 odd and 4 even in 2468"""
        code = extract_task_code('5b')
        if not code or len(code) < 10:
            pytest.skip("Task 5b code not found or incomplete")
        
        output, error = run_task_code(code, ['2468'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 0 in numbers, f"Expected 0 odd digits in output, got: {output}"
        assert 4 in numbers, f"Expected 4 even digits in output, got: {output}"
    
    def test_count_odd_even_in_1357(self):
        """Test 4 odd and 0 even in 1357"""
        code = extract_task_code('5b')
        if not code or len(code) < 10:
            pytest.skip("Task 5b code not found or incomplete")
        
        output, error = run_task_code(code, ['1357'])
        if error:
            pytest.fail(f"Runtime error: {error}")
        
        numbers = extract_numbers_from_output(output)
        assert 4 in numbers, f"Expected 4 odd digits in output, got: {output}"
        assert 0 in numbers, f"Expected 0 even digits in output, got: {output}"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])