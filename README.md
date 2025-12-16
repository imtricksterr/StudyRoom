During my first semester it was easy to waste time trying to find study rooms that would work for my schedule

I made this project over my winter break in order to circumvent that and make it a bit easier














Authentication & Policy Compliance:

I initially wanted to have a program save my login information. However, after researching the University of Connecticut IT and Automation policies, I came up with this design in order to comply with the boundaries they have stated. This program does not interact with the login processes of booking study rooms and never interacts with the widely used DUO service or any related Multi Factor Authentication. Authentication is performed manually by the user as is inputting their login credentials. 

As of today, 12/16/2025 the current version of the study room booking website has the user go to the website pick the study room, confirm the time, login/do MFA and then the user is brought back to the website to submit the booking one last time. The program I have developed automates the beginning, but once it is prompted to login it pauses and is stagnant until the submit booking pops up again. As it waits for the user to login successfully it is not doing anything with the user's computer and once the program detects that the user is back on the website it executes that remaining process for them.





This program NEVER stores or enters usernames, passwords, DUO verification codes, second party authentication credentials. It is specifically intended to serve as a booking assistant similar to a browser extension and find study rooms that meet the user's specified needs. It is simply made for educational purposes and personal productivity. No part of my StudyRoom repository has been developed with bypassing system controls, reservation limits, fairness mechanisms, and/or terms of service in mind.

This project is also not and never will be intended for unattended/large scale automation(s). Users of this software are responsible for ensuring that their use complies with all applicable university policies, library rules, and terms of service. This project is not intended for unattended or large-scale automation.
