The data set we're using here is an anonymized Web server log file from a public relations company whose clients were DVD distributors.
The logfile is in Common Log Format:

10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b
Where:

%h is the IP address of the client
%l is identity of the client, or "-" if it's unavailable
%u is username of the client, or "-" if it's unavailable
%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
%>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
For each of the problems, we would like you to write a MapReduce job to solve the problem and when you have done that you should be able to answer the below questions:
*Give the number of hits for each different file on the Web site
*Give the number of hits made by each different IP address
*Find the most popular file on the website: that is, the file whose path occures most often in access_log.
Your reducer should output the file's path and the number of times it appears in the log.
IMPORTANT: Some pathnames in the log begin with "http://www.the-associates.co.uk". Be sure to remove the portion  "http://www.the-associates.co.uk" from pathnames in 
your mapper so that all occurences of a file are counted together.