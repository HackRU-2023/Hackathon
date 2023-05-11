import { useState } from "react";

import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <p className="bg-red-400">hello worrld</p>
        <p>count is + {count}</p>
        <button onClick={() => setCount(count + 1)}></button>
      </div>
    </>
  );
}

export default App;
