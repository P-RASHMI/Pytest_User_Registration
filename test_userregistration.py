'''
@Author: Rashmi
@Date: 2021-09-29 10:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-29 12:56
@Title :Write a Python program test cases for user registration using pytest'''
from Regexvalidpytest import Validation_User
   
def test_firstname_true():
    '''
    Description:
        The given valid first name returns true in this test case.
    '''
    list1 = ["Ravali","Rashmi","Hruthik","Charishma"]
    for name in list1:
        assert Validation_User.validate_name(name) == True
    
def test_firstname_false():
    '''
    Description:
        The given invalid first name returns false in this test case.
    '''
    list1 = ["Ra","rashmi"," "]
    for name in list1:
        assert Validation_User.validate_name(name) == False
    
# def test_Invalidfirstname_Raise_exception(self):   
#     '''
#     Desription:
#         The given invalid first name should raise exception in this test case.
#     '''
#     self.assertRaises(Exception)

def test_lastname_true():
    '''
    Description:
        The given valid last name returns true in this test case.
    '''
    list1 = ["Pulmamidi","Radhee"]
    for name in list1:
        assert Validation_User.validate_name(name) == True

def test_lastname_false():
    '''
    Description:
        The given invalid last name returns false in this test case.
    '''
    list1 = ["#Pulmamidi","","@1234"]
    for name in list1:
        assert Validation_User.validate_name(name) == False

def test_emailid_true():
    '''
    Description:
        The given valid email id returns true in this test case.
    '''
    list1 = ["abc.xyz@bl.co.in","ras@gmail.com"]
    for email in list1:
        assert Validation_User.validate_email(email) == True
    
def test_emailid_false():
    '''
    Description:
        The given invalid email id returns false in this test case.
    '''
    list1 = ["rashmi25@gmailcom","r@m",""]
    for email in list1:
        assert Validation_User.validate_email(email) == False


def test_phonenumber_true():
    '''
    Description:
        The given valid phone number returns true in this test case.
    '''
    list1 = ["91 9812056239","91 8954321208","91 9892388991","91 8923617777"]
    for phone in list1:
        assert Validation_User.validate_phone_number(phone) == True

    
def test_phonenumber_false():
    '''
    Description:
        The given invalid phone number returns false in this test case.
    '''
    list1 = ["88 1235799021","72125647389212","12 9812780910"," "]
    for phone in list1:
        assert Validation_User.validate_phone_number(phone) == False
    
def test_passwordall_true():
    '''
    Description:
        The given valid password returns true in this test case.
    '''
    list1 = ["Ravadh@02","XHava+1234","AbcdEG12^4"]
    for password in list1:
        assert Validation_User.validate_password(password) == True

def test_passwordall_false():
    '''
    Description:
        The given invalid password returns false  in this test case.
    '''
    list1 = ["1235799021","ARjunAKRISHN",""]
    for password in list1:
        assert Validation_User.validate_password(password) == False

    