# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
**What This Program Aims to Solve:**
* Produce a functioning web crawler that uses recursion. Use exception handling to create a solution that will return helpful exceptions rather than crashing.

**What a Good Solution Looks Like:**
* A good solution is a crawl() method that can use recursion to search a provided URL for hyperlinks and follow and report them to a specified depth.
* The program does not crash when bad input is supplied, it gives the right exceptions.
* Use Third party libraries to identify hyperlinks instead of re-inventing the wheel.

**Any Challenges that I can forsee:**
* We've barely been taught anything about url's or websites so that's going to be difficult
* The assignment description is excessively long so keeping track of all of it is going to be a nightmare.
* Leveraging third party libraries takes time to figure out how they are used and there's like 4 on this assignment alone. Thanks.
* I don't know how to implement Control-C yet so that's going to be difficult.

## Phase 1: System Analysis *(10%)*

**Data Used by the Program:**
* From the command line, the program takes, a URL, the maximum depth to recursively search for hyperlinks.
* Uses the third party libraries "requests", "BeautifulSoup", "urlparse, urljoin" from bs4, and some others.
* Uses the hyperlinks on websites

**What Form the Output Will Take:**
* Once Errors are encountered, the program handles the exceptions and terminates without crashing.
* Assuming that no errors are encountered and the proper input is supplied:
  * The first line of the output is: Crawling from [supplied website] to a maximum distance of [supplied depth] link
  * The lines thereafter are all of the websites that the program found and visited.

**What Algorithms and Formulae:**
* crawl(url, depth, maxdepth, visited[]) method:
  * starts at the provided url parameter
  * After each site thereafter it:
    * calls itself again with depth + 1 and adds the site to the 
    visited[] array if the depth is less than maxdepth.


## Phase 2: Design *(30%)*

**Function Signatures:**
```python
def crawl(url):
    emptyVisitedList = []
    #second parameter is starting at depth of 1, third parameter is the maximumdepth of 3, emptyVisitdList will be changed after each recursive call
    crawlRecursiveHelperMethod(url, 1, 3, emptyVisitedList)

def crawlRecursiveHelpterMethod(url, depthAlreadyAt, MaximumDepth, visitedSiteList):
    # Base cases checked at the beginning, return if we've gone past the max depth or there are no hyperlinks on the page.
    if(no new hyperlinks are found) or (maximum depth is reached) or (url is in visitedSiteList):
        return
    else:
        try :
            # Try this, not sure how to use keyBoardInterrupt yet 
            # Print the current URL with indentation to indicate what level we are at
            print("\t" + url)
            # This was in the starter code. It checks to see if I have access to the link, prints an error code if I don't,
            # Finds the hyperlinks in the document with the beautifulsoup call, finds the one specific to 'a'
            # goes through each of the links with 'a' and creates an absolute URL since that link is a relative URL
            # This code printed the absoluteURL at the end, my code printed the URL in the beginning, so where the starter code
            # printed the link, I'm going to do a recursive call to the link instead ( lines 78, 79 ).
            
            response = requests.get(url)  	         	  
    if not response.ok:  	         	  
        print(f"crawl({url}): {response.status_code} {response.reason}")  	         	  
        return  	         	  

    html = BeautifulSoup(response.text, 'html.parser')  	         	  
    links = html.find_all('a')  	         	  
    for a in links:  	         	  
        link = a.get('href')  	         	  
        if link:  	         	  
            # Create an absolute address from a (possibly) relative URL  	         	  
            absoluteURL = urljoin(url, link)  	         	  

            # Only deal with resources accessible over HTTP or HTTPS  	         	  
            if absoluteURL.startswith('http'):  	         	  
                # print(absoluteURL)  	  
                crawlRecursiveHelpterMethod(absoluteURL, depthAlreadyAt + 1, MaximumDepth, visitedSiteList.append(absoluteURL))
            
                
                # The line above this has the recursive call. The absoluteURL is passed in, along with increasing the depthAlreadyAt by 1,
                # The MaximumDepth remains the same, and we need to add the absoluteURL to the sights we visited already.
```
**if __name__ == '__main__:'**

```python
    ## If no arguments are given...  	         	  
    if len(sys.argv) < 2:  	         	  
        print("Error: no URL supplied", file=sys.stderr)            #Starter Code
        exit(0) 
    else:  	         	  
        url = sys.argv[1]  	 
        #use urlparse to determine if it is an absolute URL, probably better to use a try and exception block here
        if (url is not an absoluteURL):
            print("Error: Invalid URL supplied. \n Please supply an absolute URL to this program")
            sys.exit
            
        optionalDepthOverride = input("Enter [integer] to override Depth of 3 or [S] to skip")
        
         # What time did the program start
        beforeTime = time.time()  	  
        
        try:
            if optionalDepthOverride == "S":
                #Run crawl with 3 as MaximumDepth
            else:
                #Run crawl with the the inputted integer as the maximum depth
        except:
            #handle the error

        plural = 's' if maxDepth != 1 else ''  	            #I don't know what this means right now, I'll try to figure it out later        	  
        print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	    	  
    
        after = time.time()
        #print out how much time it took to run the crawl function recursively
```

**What Happens in the Face of Good Input:**
* If there is no URL initially given or the URL given is not an absolute URL, the program gives a helpful error message without crashing
* Otherwise, if the URL is absolute, the program opens it, and recursively prints out the hyperlinks to 3 levels, indented accordingly

**What Happens in the Face of Bad Input:**
* The program crashes if bad input is supplied
* The program gets stuck in a recursion loop

**Specific examples that occured to me:**
* I emailed Falor asking where the urlparse is implemented because it wasn't clear, but I figured it out once I revied the "__main__" section:
  * It is needed to check to see if the supplied URL is absolute or not.
* I still don't understand how this program is being run from the command line because I don't know what the __name__ variable is.

## Phase 3: Implementation *(15%)*

**More or Less Working Code:**
```python
def crawlRecursive(url, currentDepth, maxDepth, visitedList):    
    # The instructions say that parse has a function that does this, but this will work the same way since sites that have
    # everything the same except for the fragments are the same site.
    if "#" in url:
        url = url[:url.find("#")]               
        
    # This is 'opening' the site
    response = requests.get(url)
    if not response.ok:
        print(f"crawl({url}): {response.status_code} {response.reason}")
        return

    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    print("    " * currentDepth + url)

    before = time.time()
    for a in links:
        link = a.get('href')
        if link:
            # Create an absolute address from a (possibly) relative URL
            absoluteURL = urljoin(url, link)
            # I didn't realize that this is appending all the sites into visitedList before they are even opened so the count would be too high
            if currentDepth > maxDepth or url in visitedList:
                return
            visitedList.append(url)
            # Only deal with resources accessible over HTTP or HTTPS
            if absoluteURL.startswith('http'):
                crawlRecursive(absoluteURL, currentDepth + 1, maxDepth, visitedList)
        
    # I just wasn' thinking here. I forgot this was using recursion so I tried timing the "meat" of the program which was lines 153-164.
    # Timing it needs to go in the main method before and after crawlRecursive is called.
    after = time.time()
    totalTime = after - before
    print("The runtime was: " + totalTime)
            

    # I didn't know how to use the try and exception block so I didn't put those in until I got help

# We weren't taught what this is, but apparently when the program sees this, it starts here instead of at the beginning.
if __name__ == "__main__":

    ## If no arguments are given...
    if len(sys.argv) < 2:
        print("Error: no URL supplied", file=sys.stderr)
        sys.exit(0)
    else:
        url = sys.argv[1]
        visitedList = []
        maxDepth = 3

    # If there is a third parameter from the command line and it is an integer, assign it to maxDepth
    if len(sys.argv) > 2:
        givenInt = int(sys.argv[2])
        if isinstance(givenInt, int) and givenInt >= 0:
            maxDepth = givenInt

    # If the url doesn't have a scheme or location, then stop, otherwise, run the recursion.
    # I originally had this in the crawlRecursive() method but I don't need to parse every site after the first one because they
    # are already hyperlinks.
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print("Error: Invalid URL supplied")
        print("Please supply an absolute URL to this program.")
        sys.exit(0)

    else:
        # didn't have this enclosed in a try/except blocks so the Control C option to quit didn't work.
            print(f"Crawling from {url} to a maximum depth of {maxDepth}")
            crawlRecursive(url, 0, maxDepth, visitedList)
            totalTime = after - before
            sys.exit(0)
```
**Things I learned:**
* The server is really hard to work with, I'm using a Windows computer, so there is an error with the server when using it. I spend over an hour with the tutor lab while they talked over my issue, they even pulled up their own code from years ago to try to get it working.
  * They couldn't figure it out, so I turned to Professor Falor and the TA's. Professor Falor addressed it in the mass announcement but even with a large -timeout [time] it wasn't working. I played with many timeout values but it still was bugged. The tutor lab is closed for the semester and idk what else to do.
* Timing the process should be outside of the recursive method because otherwise it's just going to get called over and over again
* "if __name__ == __main__" means that the program will start there instead of starting at the beginning. (Python automagically starts at line 0)


## Phase 4: Testing & Debugging *(30%)*

**Test Cases Ran on My Computer:**
* I tested my code mainly from the command line with:
  * python src/crawler.py https://cs.usu.edu 1
  * This worked very well because I had a general idea of what it was supposed to output and it did so through running this.
* Eventually, I tried to run my code with the server. Because I am a Windows User, the server was not happy with me at all for some reason. Falor said it's because my computer is too slow but my HP Pavilion has the i7 processor, and is only 1 year old so I don't know.
* Because this was not working at all, I spent hours in the debugger as well trying to figure out if what was wrong was on my end.
* Falor said that my code was printing some duplicates in the server but on every case I run it on the terminal or in the IDE, there are NO duplicates, I've ran through my code many times and cannot find how it would be producing a duplicate. I honestly think that the server is not working properly.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

* Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
      * I don't believe any parts are slopily written. The code about from the starter code is difficult to understand but doable.
    * Are there parts of your program which you aren't quite sure how/why they work?
      * All of the stuff in the starter code. I understand how it is implemented, and how to manipulate it, but I don't understand any of the meat of it.
    * If a bug is reported in a few months, how long would it take you to find the cause?
      * Probably 10 minutes. This code isn't very long and is pretty self explanatory.
    * Will your documentation make sense to...
        * ...anybody besides yourself?
          * most likely. The names that are used are very well done and the logic is sound, and its a short program.
        * ...yourself in six month's time?
          * probably, I spend mf'ing HOURS upon HOURS on this freaking assignment whether it was with the tutor lab, or with erik falor, or with my dad on facetime trying to figure it out. (He is a software engineer)
    * How easy will it be to add a new feature to this program in a year?
      * super easy, its a small program
    * Will your program continue to work after upgrading...
        * ...your computer's hardware?
          * I don't know enough to make a decision about this one. Probably, assuming that the main parts don't change.
        * ...the operating system?
          * Same comment as above, I don't have enough knowledge about the OS.
        * ...to the next version of Python?
          * Probably, assuming that the main parts of it don't change. There are things that are from third party library which will obviously remain the same but their compatability might change.
* Fill out the Assignment Reflection on Canvas.
  * "I feel God in this Chillis tonight"
  * if you understand this reference, you owe me 5 extra points
