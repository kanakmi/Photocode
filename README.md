# Photo code

## Demo Video
- Link for the demo video: https://youtu.be/Yp0J-6vJ4Eg

## 💡 Inspiration

There are multiple inspirations behind this project

- When doing competitive programming on any platform, it happens with all of us that while solving the problem, we try really hard but are unable to crack the solution but then, in a completely different setting, out of nowhere, a new approach hit us in our mind. Mostly when it happens, we are in a situation where we do not have immediate access to a system to test our strategy.
- When the pandemic hit us, there were so many individuals who wanted to start their hacker journey but couldn't due to financial constraints.

## 💻 What it does

Our project aims to empower hackers around the globe to run their code on a mobile device by writing it on paper and then clicking its picture. The OCR algorithm analyzes and extracts the code from the image and pastes it into an editor where the user could make final modifications before compiling and running the code.

Other features include -
- Programing languages available to compile:
    - C++
    - C
    - Javascript
    - Java
    - Python
- Opportunity Section - Lets users explore various career opportunities they can apply to.
- Blog Section - Lets users read blogs from various sources and share their thoughts.
- Tutorials Section - Provides links to some useful tutorials on multiple topics users can refer to if they get stuck.

## ⚙️ How we built it

- Django: For backend
- Tesseract: For OCR
- Python: For backend
- HTML and CSS: For frontend
- Hedera: For smart contract
- Symbl.ai API: for speech to text

## ☁️ Use of Linode

We have a dedicated Linode server for our backend. We use it for hosting our website and for storing our data. Linode Block Storage allows users to extend their server storage capacity with volumes on demand. Linode Backup allows us to back up their servers on a daily, weekly, or monthly basis which makes it easy and efficient. Linode allows users to manage multiple server instances across a single system.

## 🔐 Best Blockchain Project Using Hedera

We are using Hedera for checking the contract calls. Hedera is a decentralized public network that utilizes the Hashgraph consensus algorithm to overcome the traditional limitations of blockchain and allow one to create the next era of fast, fair, and secure applications.

## 🤖 Symbl.ai

- We are using Symbl.AI API to convert speech to text for the search pages. The user can convert his speech to text in the IDE (for writing the code).  
Commands:  

- To clear workspace 
```
clean canvas 
```
- To remove last word  
```
remove last word
```
- To execute code
```
Execute code  
```

## 🍻 Dream Big and Create More Cheers with AB InBev
- We dream to make this app available to all people who have limited access and want to learn to code and make their dream come true to learn to code.

## 🧠 Challenges we ran into

- We have some challenges with the backend, but we managed to get the project done.

## 🏅 Accomplishments that we're proud of

- Completing the project within the given time frame.
- Creating a fully functional application.
- Creating OCR algorithm analyzes
- Building an IDE.

## 📖 What we learned

- Using Symbl.ai's Speech to Text service.
- How to use Hedera for the smart contract.

## 🚀 What's next for PhotoCode

- Adding more features to the application.

## Installing and Running

- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Go to server directory and do ```npm install``` ```node index.js```
- In the main directory do ```python manage.py runserver```
