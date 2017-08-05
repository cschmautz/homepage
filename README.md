# homepage  
My personal homepage codebase, located at 
[www.christopherschmautz.com](www.christopherschmautz.com).  
  
## technology  
This site uses very basic Flask features for setting up a simple content 
delivery system for my static images and text. Jinja is heavily leveraged for 
page reuse, by extending a base page layout to the children templates, using 
markdown to inject the content into the rendering form.  
  
I chose to not go the JavaScript route as a longtime user of 
[NoScript](https://addons.mozilla.org/en-US/firefox/addon/noscript/). 
Much of the popular web is based on JavaScript so I may change this in the 
future, but for now, Jinja's templating engine for a project of this size 
is a sensible solution.  
  
The entire site consists of a read-only data file, in which all the metadata 
for all my posts and the site in general are stored, similar to a NoSql store, 
but even more rudimentary. I chose this format due to the ease of editing the 
flat file while on different machines (I store the file in Google Drive) but 
also chose this implementation for the simplicity of upkeep.  
  
My site doesn't store any other content at this time, and so a database 
solution isn't needed. In the future case of handling user comments, I may 
opt in to using a database to store those documents.  
  
## notice of MDL library usage  
For the front end library, I am relying heavily on 
[Material Design Lite by Google](https://getmdl.io). I like their design and 
overall the library is fairly easy to use. I will freely admit to having used 
one of their [templates](https://getmdl.io/templates/index.html) to start out 
the framework, and tweek accordingly, as the site was being thrown together in 
a short timeframe before PyCon 2017.  
  
Since Material Design Lite is 
[entering it's twighlight years](https://github.com/google/material-design-lite#limited-support) 
in favor of [Material Components for the Web](https://github.com/material-components/material-components-web), 
I will eventually be making the switch over to the newer framework.  
  
MDL adheres to staying away from JavaScript as I intended to with the site, 
and overall is a pleasure to work with! You can find more information in the 
linked references below.  
  
## references  
[Material.io Design Guidelines](https://material.io/guidelines/)  
[Material.io component demos](https://material-components-web.appspot.com)  
[Material Design Lite components (deprecated)](https://getmdl.io/components/index.html)  
