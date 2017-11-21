from palindrome_base import is_palindrome, get_base
import pytest

def test_one_digit():
	assert is_palindrome('1')

def test_not_palindrome():
	assert not is_palindrome('12')

def test_not_palindrome_same_digits():
	assert not is_palindrome('123231')

def test_even_palindrome():
	assert is_palindrome('123321')

def test_odd_palindrome():
	assert is_palindrome('1235321')

def test_get_base_2():
	assert get_base(2, 2) == str(10)

def test_get_base_3():
	assert get_base(3, 3) == str(10)

def test_get_base_5():
	assert get_base(5, 5) == str(10)