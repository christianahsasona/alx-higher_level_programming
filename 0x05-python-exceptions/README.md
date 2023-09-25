<h1>0x05. Python - Exceptions</h1>
<p> here are (at least) two distinguishable kinds of errors: syntax errors and exceptions. </p>
<h2> Syntax Errors </h2>
<p> Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python </p>
<code> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
</code>
<h2> Exceptions </h2>
<p> Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs</p>
<h2> Handling Exceptions </h2>
<p> It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception. </p>
<code> while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...") 
</code>
<p> The try statement works as follows.</p>
<ul>
<li>
First, the try clause (the statement(s) between the try and except keywords) is executed.
</li>
<li>
If no exception occurs, the except clause is skipped and execution of the try statement is finished.
</li>
<li>
If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.
</li>
<li>If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.</li>
