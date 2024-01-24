#!/usr/bin/python3  	         	  

#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  


# pip install --user requests beautifulsoup4  	         	  
import requests  	         	  
from bs4 import BeautifulSoup  	         	  
from urllib.parse import urlparse, urljoin  	         	  
import sys  	         	  
import time  	         	  


def crawl(url):
    visitedList = []
    crawlRecursive(url, 0, 3, visitedList)

def crawlRecursive(url, currentDepth, maxDepth, visitedList):
    if currentDepth > maxDepth:
        return

    # Trim whatever is after the pound sign
    if "#" in url:
        url = url[:url.find("#")]

    try:

        # If I don't have access to the url...
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        # We don't want to visit the same URL twice
        if url in visitedList:
            return
        else:
            visitedList.append(url)

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        print("    " * currentDepth + url)

        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)

                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    crawlRecursive(absoluteURL, currentDepth + 1, maxDepth, visitedList)

    except KeyboardInterrupt as K:
        print(f"Interrupted by keyboard input {K}")
        sys.exit(0)
    except Exception as e:
        print(f"Seach failed because {e}")


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
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print("Error: Invalid URL supplied")
        print("Please supply an absolute URL to this program.")
        sys.exit(0)

    else:
        try:
            before = time.time()
            print(f"Crawling from {url} to a maximum depth of {maxDepth}")
            crawlRecursive(url, 0, maxDepth, visitedList)

        except KeyboardInterrupt:
            print("Lol bye")
            print("Interrupted by keyboard input")
        finally:
            after = time.time()
            totalTime = after - before
            print("   ...   ")
            print(f"Visited {len(visitedList)} unique pages in {totalTime} seconds", file=sys.stderr)
            sys.exit(0)



