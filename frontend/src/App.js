import logo from './logo.svg';
// import './App.css';
import './App.scss';
import GetData from './Components/GetData';
import Speedometer from './Components/Speedometer';
import Navigation from './Components/Navigation';
import CryptoInfo from './Components/CryptoInfo';
import { useState } from 'react';

function App() {

  const [isLineGraph, setLineGraph] = useState(true)

  const SetGraphs = () => {
    if(isLineGraph) {
      setLineGraph(false);
    } else if (!isLineGraph){
      setLineGraph(true);
    }

  }

  return (
    <div className="App bg-pri">
      <div>
        <Navigation />
      </div>
      <div className='mx-4'>
        <GetData isLineGraph={isLineGraph}/>
      </div>
      <div className='my-4 container align-items-center justify-content-center col-md-5'>
        <div className='row justify-content-center'>
          <div className='col-md-6 text-center'>
            {isLineGraph ? <button id='button' onClick={SetGraphs}><h4>Switch to Candle Stick Graph</h4></button>: <button id='button' onClick={SetGraphs}><h4>Switch to Line Graph</h4></button>}
          </div>
        </div>
      </div>
      <div className='bottom-section bg-sec d-flex flex-row border-top border-white'>
        <div className='container-fluid align-items-center justify-content-center w-50 border border-white'>
          <Speedometer />
        </div>
        <div className='container-fluid w-50 border border-white p-0'>
          <CryptoInfo />
        </div>
      </div>
    </div>
  );
}

export default App;
