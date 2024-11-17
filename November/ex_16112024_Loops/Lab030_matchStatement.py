"""
match statement--same as swith in java
match variable_name:
      case pattern1:
          code block
      case pattern2:
           code block
"""

#write a program in which browser she want to run the automation

browser_name= input("enter the browser name:")
match browser_name:
    case "google":
        print("run in google browser")
    case "chrome":
        print("run in chrome browser")
    case "brave":
        print("run in brave browser")
    case "edge":
        print("run in edge browser")
    case "firefox":
        print("run in firefox browser")
    case _: # default-->not matched case
        print("no browser found")