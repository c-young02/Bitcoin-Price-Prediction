import logo from './logo.svg';
// import './App.css';
import './App.scss';
import GetData from './Components/GetData';
import Speedometer from './Components/Speedometer';
import Navigation from './Components/Navigation';
import CryptoInfo from './Components/CryptoInfo';

function App() {

  return (
    <div className="App bg-pri">
      <div>
        <Navigation />
      </div>
      <div className='mx-4'>
        <GetData />
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
