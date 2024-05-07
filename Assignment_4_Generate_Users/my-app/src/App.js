// import logo from './logo.svg';
import './App.css';
//import axios from "axios";

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <div>
        {/*Title with three paragraphs underneath*/ }
        <div>
  <h1 style={{backgroundColor: 'rgb(252, 1, 1)'}}>  </h1>
  <p> My name is Michael Herman and this is my About Me page. 
    <br />
    A little fun fact about me is that I was born in Guatemala. I came to the US when I was about 4 years old. Me and my family usually try to go back to Guatemala to vist family every year during the summer.  I can speak English and Spanish. Some other languages that I have learned was French but I don't remember that much any more. I was learning Japanese this semester but had to drop it because of my other classes and their workload but it was fun. 
    I also like to play video games. I made a list of some of the video games that I like to play. I also made a list of some places that I like to eat at. I'm a Christian. I also play a musical instrument. I play the drums. I'm part of the worship team at my church and I play the drums also whenever its my turn to play.   
  </p>

  <br />
  <hr />

  <h3>Video Games</h3>
  <p>Here is a list of some games that I like to play:</p>
  <div className="section">
    Games played the most:
  </div>

  <ul>
    <li>Halo (Franchise) </li>
    <li>Skyrim</li>
    <li>Fallout 4</li>
    <li>Legend of Zelda Breath of the Wild and Tears of the Kingdom</li>
    <img src="Images\Halo image.jpg" alt="Fallout Cover" /> 
    <img src="Images\Halo image.jpg" alt="Halo Cover" /> 
  </ul>

  <hr />

  <h3>Fast Food</h3>
  <p>Here is a list of fast food places that I like to eat at. </p>

  <div className="section">
    Places I like to eat at:
  </div>

  <li>Taco Bell</li>
  <li>Chick Fil-a </li>
  <li>Canes</li>
  <li>In &amp; Out</li>
  <img src="Images\Taco Bell.png" alt="TacoBell logo"/>

  <br />
  <hr />

  <a href="https://github.com/MKHerman117/CSE_4500_Platform_Computing_Repo/blob/main/Assignment_1_About_Me_Page/README.md">Github Link</a>
  <a href="https://github.com/MKHerman117/CSE_4500_Platform_Computing_Repo/blob/main/Assignment_1_About_Me_Page/README.md"><button>Click Me</button>
  </a></div>
        </div>
      </header>
    </div>
  );
}

export default App;
