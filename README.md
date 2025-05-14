**Feelings Logger** is a GUI-based desktop application that allows users to log their emotions<br> by clicking on images representing different feelings. 
<br> 

Built-in modules that are used are: <br>
- MySQL Connector → storing user data and logged emotions
- bcrypt → Used for hashing passwords securely for signup/login functionality
- Tkinter → GUI  
- Matplotlib → Charts  
- Pillow → Image handling
- requests → interacting with APIs

🔐 Users can register and log in to the application. <br>
📥 All data, including user credentials, logged emotions, associated messages and emotion types, is stored in a relational database *feeldb*.<br>
📊 The app also provides an analysis feature that displays bar and pie charts of logged emotions over time.<br>
💬 Based on chosen feeling, app displays message of support.<br>
🔍 Users can now filter logs by emotion or date to easily track their emotional history. <br>
⛅ New feature: retrieve weather info from an online API to display an icon of the current weather condition within the app's GUI. <br>
🔜 Upcoming features are: 
- exporting logging history and charts to pdf.<br>

⏳ **Status**: In progress 
