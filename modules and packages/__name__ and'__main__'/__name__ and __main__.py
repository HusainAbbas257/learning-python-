import example

example.sayhi()
# just a simple call but its output is"
# hi from sayhi()
# hi from sayhi()

# it runs example.py 2 times once while importing and once while calling it to prevent this we can use __name__ it tells from where it is being called

# now if you try to imort example2.py  it will almost do the same except one thing
import example2
example2.greet()


# using this u can specify codes to run when called directly or when called indirectly