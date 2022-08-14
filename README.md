# CARA - Virtual Assistant

### DESCRIPTION 

The aim of the project is to design a virtual assistant with voice input and output that can perform basic functions like web browsing, playing music,opening applications etc. On interfacing with sensors and hardware, it is capable of performing home automation features also. This project was done as a part of Object Oriented Analysis and Design (CS7503).The home automation features implemented here have a hard coded temperature/ water level value which can be automated to be taken from home automation devices. Design Patterns are used and UML diagrams are drawn. The diagrams can be found on the CaraReport.docx file.

### SOFTWARES USED

- Enterprise Architect- UML Modeling

- Visual Studio Code- Implementation

### LANGUAGE USED

Python

### DEPENDENCIES NEEDED

- pyttsx3 

- speech_recognition 

- wikipedia

- webbrowser

- smtplib

- zope.interface

To install the above mentioned dependencies use:

- pip install pyttsx3
- pip install speech_recognition
- pip install wikipedia
- pip install webbrowser
- pip install zope.interface

### HOW TO RUN CARA

Use python cara_app.py to run the file

### CLASS DIAGRAM AND DESIGN PATTERNS

![alt text](https://github.com/charanya78/cara_virtual_assistant/blob/main/diagrams/class_diagram.png)

The classes implemented along with their uses:

- User:

  - **Parameters** - username, password, cara_id, security_code
  - **Methods** - constructor
  - **Uses** - Used to set up CARA device and link with physical device
  - **Further extensions** - Change password, add user

- CaraApp:

  - **Methods** - enableVoiceInput
  - **Uses** - Used to enable voice input
  
- UserInterface:

  - **Methods** - wishMe
  - **Uses** - Used to wish the user 
  
 - WebServer:

    - **Methods** - search_web, sendEmail, map_queries, orderfood
    - **Uses** - Used for for web search related queries like google, wikipedia, maps and mail
    - **Further extensions** - orderfood could be extended to place an order

  - SoundSystem:

    - **Methods** - takeCommand, speak
    - **Uses** - Takes commands from user and recognize
  
  - Operation:

    - **Methods** - setDevice, resetDevice
    - **Uses** - To set up cara device and reset function

  - PlayMedia:

    - **Methods** - playMusic, playVideo
    - **Uses** - To play music and video

   - Home_Automation(Interface):

      - **Methods** - enable_device, disable_device
      - **Uses** - To allow device _control and security_system to extend
      - **Further extensions** - Smart Home, More Device Controls
  
  - Device_Control (Extended from Home_Automation):

    - **Methods** - enable_device, disable_device
    - **Uses** - To allow TV and AC to inherit
    
   - Security_System (Extended from Home_Automation):

      - **Methods** - enable_device, disable_device
      - **Uses** - To allow Fire_Alarm and Emergency to inherit
      
   - TV (Extended from Device_Control):

      - **Methods** - enable_device, disable_device, change_volume,c hange_channel
      - **Uses** - To change colume and channel
      
   - AC (Extended from Device_Control):
   
      - **Methods** - enable_device, disable_device, changemode, changetemp
      - **Uses** - To change mode and temperature

   - Fire_Alarm (Extended from Security_System):
    
      - **Parameters** - waterlevel_ts
      - **Methods** - checkwaterlevel, monitor, makecall, spriklewater
      - **Uses** - To check if water level is less than the threshold

   - Emergency (Extended from Fire_Alarm):
    
      - **Parameters** - waterlevel_ts
      - **Methods** - makecall, spriklewater
      - **Uses** - To make a call / sprinke water in case of emergency
        
   - Conventional (Extended from Fire_Alarm):

      - **Methods** - monitor
      - **Uses** - To monitor temperature levels

   - Camera_Control (Extended from Security_System):
    
      - **Methods** - img_capture,img_delete
      - **Uses** - To capture and delete images from CCTV

Design patterns like Factory, Prototype, Bridge were used in the implemention. Other UML diagrams ike activity diagram, state digaram can be found in the document.
