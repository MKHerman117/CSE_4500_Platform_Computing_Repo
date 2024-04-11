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
  <p> My name is  and this is my About Me page. 
    <br />
    A little fun fact about me is that I was born in Guatemala. I can speak English and Spanish. Some other languages that I have learned was French but I don't remember that much any more. I was learning Japanese this semester but had to drop it because of my other classes and their workload but it was fun.  
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
    {/* <img src="Images\Fallout_4_cover_art.jpg" alt="Fallout Cover" /> */}
    {/* <img src="Images\Halo image.jpg" alt="Halo Cover" /> */}
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
  {/* <img src="Images\Taco Bell.png" alt="TacoBell logo"/> */}

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
