import logo from './logo.svg';
import './App.css';
import GetData from './Components/GetData';
import Speedometer from './Components/Speedometer';

function App() {

  return (
    <div className="App">
      <div>
        <GetData />
      </div>
      <div>
        <Speedometer />
      </div>
    </div>
  );
}

export default App;
