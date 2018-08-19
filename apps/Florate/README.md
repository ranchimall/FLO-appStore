# FloRate-Dapp
This D-App is based on Flo  Block Chain and is used to communicate the progress of Interns in the form of Rating.<br />
<b>Usage</b><br />
To use the application we use the command python3 rating-client.py<br />
After Starting GUI choose the role:<br />
<ul>
  <li>
    If role is Employee We need to create Ratings so that they are in desired writting format.<br />
The Intern Create Ratings window contains 2 parts<br />
  <ul>
    <li>
      Intern Data: Here we choose the required Interns to be rated and press the right arrow Button<br />We then 
Enter the Ratings and submit
    </li>
    <li>
      Rating Data: Here we find all the assigned Ratings displayed and when we find they are good we finalize them by pressing on finalize button
    </li>
    </ul>
    Once The Ratings are Written we enter the Transaction Id and click post rating button to Post the ratings.
    After this the trasnaction id to be shared with interns is displayed on CLI as well as saved onto RatingData.txt
  </li>
  <li>
    If the role in Intern we just Enter the Transaction id provided by Employeer and retrieve the Ratings by clicking Fetch Rating Button
  </li>
 </ul>



