#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import math

urls = (
	'/prime/(.*)', 'is_prime'
)

app = web.application(urls, globals())


class is_prime:
	def GET(self, prime):
	    output = '{number:"'+prime+'", prime:"';
	    prime = int(prime);
	    if prime % 2 == 0 and prime > 2: 
		output+='false"}'
		return output;
	    for i in range(3, int(math.sqrt(prime)) + 1, 2):
		if prime % i == 0:
		    output+='false"}';
		    return output
	    output+='true"}'
	    return output


if __name__ == "__main__":
    app.run()
