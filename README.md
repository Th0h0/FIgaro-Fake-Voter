# FIgaro-Fake-Voter
<p><br />Ce programme utilise l'&eacute;mulation d'un navigateur web afin de soumettre des votes artificiels au sondage du site Figaro de votre choix.</p>
<p>This python software uses browser emulation to submit artificial votes to the Figaro's survey of your choice.<br /><span style="color: #ff0000;">/!\</span> This program is only meant to be a <strong>proof of concept</strong> application.</p>
<p>&nbsp;</p>
<a href="https://ibb.co/hyBBwgk"><img src="https://i.ibb.co/MsccQgb/Capture.png" alt="Capture" border="0"></a>
<p>&nbsp;</p>
# Program-requirements : 
<ul>
<li><span style="font-size: 13pt;">Latest version of Chrome&nbsp;</span></li>
<li><span style="font-size: 13pt;">Python 3</span></li>
<li><span style="font-size: 13pt;">PC running Windows</span></li>
<li><span style="font-size: 13pt;">Medium/High quality proxies</span></li>
<li><span style="font-size: 13pt;">PyQt5 and Selenium librairies (You can download them with the following command : <em>pip install PyQt5 &amp; pip install</em> <em>Selenium)</em></span></li>
</ul>
# How-to-use-the-program:
<li><span style="font-size: 13pt;">Type/paste the figaro's survey URL in the required field</span></li>
<li><span style="font-size: 13pt;">Select "Yes" or "No" depending on which votes you want the program to submit on the survey you chose</span></li>
<li><span style="font-size: 13pt;">Use the slider widget in order to specify how many artificial votes you want the tool to submit</span></li>
<li><span style="font-size: 13pt;">Paste your proxies, they can be public/private/scraped one, be careful though, since low quality proxies can make the software working extremly slowly or make it not working at all !&nbsp;</span></li>
<li><span style="font-size: 13pt;">Last step : click on the big button LAUNCH :)&nbsp;</span></li>
</ul>
# How does the program work : 
<p><span style="font-size: 13pt;">The program's GUI has been entirely made through <strong>PyQt5</strong>, mostly with Qt Designer tool.<br />The tool relies on <strong>Selenium</strong> library in order to emulate a browser able to submit the votes.<br />In order to be efficient, the program also relies on <strong>proxies</strong>. Indeed one proxy is randomly chosen for each single fake vote, from the list the user pastes, in order to make the web application believe that there are several differents users from differents zones submitting requests.</span></p>
