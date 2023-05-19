import "./App.css";

import apple from "./icons/apple.png";
import google from "./icons/google.png";
import astros from "./icons/astros.png";

import { useSpring, animated } from "react-spring";
import { useRef } from "react";

function App() {
  const ref = useRef(0);

  const props = useSpring({
    from: { backgroundColor: "#be7c4d" },
    to: async (next) => {
      while (true) {
        await next({ backgroundColor: "#92140c" });
        await next({ backgroundColor: "#353238" });
        await next({ backgroundColor: "#be5a38" });
        await next({ backgroundColor: "#FFBA49" });
        await next({ backgroundColor: "#ACBFA4" });
        await next({ backgroundColor: "#468189" });
        await next({ backgroundColor: "#7B5E7B" });
        await next({ backgroundColor: "#3E5641" });
        await next({ backgroundColor: "#be7c4d" });
      }
    },
    config: { duration: 3000 },
  });

  return (
    <div className="App">
      <header className="App-header">
        <div id="bouncing-box">
          <div ref={ref}>
            <h1>Cade Crandall</h1>
            <h2>Texas & Colorado based data scientist with a background in software engineering</h2>
            <h1>Work Experience</h1>
          </div>
        </div>
        <div className="icon-container">
          <img src={apple} alt="Apple" width={55} />
          <img src={google} alt="Google" width={50} />
          <img src={astros} alt="Astros" width={55} />
        </div>
        <animated.div style={props} className="animated-background" />
      

      <h1>Super Mario Timeline</h1>
        <p>Initial launch dates of games in the Super Mario series. </p>
        <ul class="timeline">
          <li><time datetime="1985-09">September 1985</time>Super Mario Brothers</li>
          <li><time datetime="1986-06">June 1986</time>Super Mario Bros:<br /> The Lost Levels</li>
          <li><time datetime="1988-10">October 1988</time>Super Mario Bros. 2</li>
          <li><time datetime="1988-10">October 1988</time>Super Mario Bros. 3</li>
          <li><time datetime="1989-04">April 1989</time>Super Mario Land</li>
          <li><time datetime="1990-11">November 1990</time>Super Mario World</li>
          <li><time datetime="1992-10">October 1992</time>Super Mario Land: 6 <br />Golden Coins</li>
          <li><time datetime="1995-08">August 1995</time>Super Mario World 2: <br />Yoshi's Island</li>
          <li><time datetime="1996-06">June 1996</time>Super Mario 64</li>
          <li><time datetime="2002-07">July 2002</time>Super Mario Sunshine</li>
          <li><time datetime="2006-05">May 2006</time>New Super Mario Bros.</li>
          <li><time datetime="2007-11">November 2007</time>Super Mario Galaxy</li>
          <li><time datetime="2009-11">November 2009</time>New Super Mario Bros. Wii</li>
          <li><time datetime="2010-05">May 2010</time>Super Mario Galaxy 2</li>
          <li><time datetime="2011-11">November 2011</time>Super Mario 3D Land</li>
          <li><time datetime="2012-07">July 2012</time>New Super Mario Bros 2</li>
          <li><time datetime="2012-11">November 2012</time>New Super Mario Bros. U</li>
          <li><time datetime="2013-11">November 2013</time>Super Mario 3D World</li>
          <li><time datetime="2015-09">September 2015</time>Super Mario Maker</li>
          <li><time datetime="2016-12">December 2016</time>Super Mario Run</li>
          <li><time datetime="2017-10">October 2017</time>Super Mario Odyssey</li>
          <li><time datetime="2019-06">June 2019</time>Super Mario Maker 2</li>
          <li><time datetime="2021-02">February 2021</time>Super Mario 3D World + Bowser's Fury</li>
        </ul>
    </header>
    </div>

  );
}

export default App;
