---
services: app-service\web
platforms: python
author: James Hovet
---

# HovetPyAppTest, or, "Better Than a Stat Project"

I made this over the course of a few days because I wanted to make something that would relate to the school, and be fun.

# How it works

So, first thing is first, there are two parts to this game, the client side (the laptop) and the server side (the server somewhere in the "cloud".) 

The client sends and recieves data, and the server does operations with that data and sends back results, basically. 

## Roadmap

1. The client sends a request to the server saying "hey, can I have the homepage."
2. The server sends back "yep! here it is."
3. If the user clicks "play the game," then the client requests the first page of the game screen
4. The server sends the game page's HTML, along with the person data that it generated randomly based on the python code
5. The client recieves the data, and then the user makes his input
6. The client sends that data to the server and the server decides if the input was correct. If so, then the cooresponding data gets added to the database, and the server sends the question page back to the client
7. repeat steps 4-6 until the results page comes up. 


Based off of a server setup project by cephalin of Microsoft

## License
Based off of a server setup project by cephalin of Microsoft
See [LICENSE](LICENSE).
