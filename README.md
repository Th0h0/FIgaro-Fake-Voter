# FIgaro-Fake-Voter
<p><br />Ce programme utilise l'&eacute;mulation d'un navigateur web afin de soumettre des votes artificiels au sondage du site Figaro de votre choix.</p>
<p>This python software uses browser emulation to submit artificial votes to the Figaro's survey of your choice.<br /><span style="color: #ff0000;">/!\</span> This program is only meant to be a <strong>proof of concept</strong> application.</p>
<p>&nbsp;</p>
<a href="https://ibb.co/hyBBwgk"><img src="https://i.ibb.co/MsccQgb/Capture.png" alt="Capture" border="0"></a>
<p>&nbsp;</p>
## Program Requirements : 

- Latest version of Chrome

- Python 3

- PC running Windows

- Medium/High quality proxies

- PyQt5 and Selenium librairies (You can download them with the following command : 

  ```pip install PyQt5 & pip install Selenium```


## How to use the program :

- Type/paste the figaro's survey URL in the required field

- Select "Yes" or "No" depending on which votes you want the program to submit on the survey you chose

- Use the slider widget in order to specify how many artificial votes you want the tool to submit

- Paste your proxies, they can be public/private/scraped one, be careful though, since low quality proxies can make the software working extremly slowly or make it not working at all ! 

- Last step : click on the big button LAUNCH :) 

## How does the program work :
- The program's GUI has been entirely made through PyQt5, mostly with Qt Designer tool.

- The tool relies on Selenium library in order to emulate a browser able to submit the votes.

- In order to be efficient, the program also relies on proxies. Indeed one proxy is randomly chosen for each single fake vote, from the list the user pastes, in order to make the web application believe that there are several differents users from differents zones submitting requests.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
