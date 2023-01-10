# pwManager
This is a password manager written in python, it uses the Qt-Framework for the GUI implementation.


I think this is not secure since the master password is also just an xor of itself. 
So it should be possible to xor the master password with itself and then decode the result of this to get the master password in clear text.
