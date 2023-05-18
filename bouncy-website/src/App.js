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
      </header>
    </div>
  );
}

export default App;
