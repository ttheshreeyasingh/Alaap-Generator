import "./App.css";
import Navbar from './components/Navbar';
import AudioPlayerWithTextForm from './components/AudioPlayerWithTextForm';
import React, { useState } from 'react';
import Alert from './components/Alert';


function App() {
  const [mode, setMode] = useState('light'); // Whether dark mode is enabled or not
  const [alert, setAlert] = useState(null);

  const showAlert = (message, type)=>{
      setAlert({
        msg: message,
        type: type
      })
      setTimeout(() => {
          setAlert(null);
      }, 1500);
  }

  const toggleMode = ()=>{
    if(mode === 'light'){
      setMode('dark');
      // document.body.style.backgroundColor = '#042743';
      document.body.style.backgroundImage = "url('./78e9639ba3c0.jpg')" ;
      showAlert("Dark mode has been enabled", "success");
    }
    else{
      setMode('light');
      document.body.style.backgroundImage = "url('./78e9639ba3c0.jpg')" ;
      // document.body.style.backgroundColor = 'white';
      showAlert("Light mode has been enabled", "success");
    }
  }

 
  return (
    <>
    <div style={{ backgroundImage: "url('./78e9639ba3c0.jpg')" }}>
      <Navbar title="Alaap Generation App" mode={mode} toggleMode={toggleMode} key={new Date()} />
      <Alert alert={alert} />
    
      <div className="App container py-3" >
        <h3>Generate Alaap Sequences using Aroh and Avroh</h3>
      </div>

      <AudioPlayerWithTextForm showAlert={showAlert} mode={mode} />
      </div>
    </>
    
  );
}  

export default App;







