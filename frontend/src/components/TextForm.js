import React, { useState, useEffect } from 'react';
// import { spawn } from 'child_process';
// import { saveAs } from 'file-saver';
// import * as FileSaver from 'file-saver';
import axios from 'axios';




export default function TextForm(props) {
    const [text, setText] = useState('Loading...');
    const [audioSrc, setAudioSrc] = useState(null);
    const [transcriptNumber, setTranscriptNumber] = useState(1);
    const [isAudio, setIsAudio] = useState(false);
    useEffect(() => {

        const fetchText = async () => {
            try {
                const response = await axios.get(`${process.env.PUBLIC_URL}/aalaap.txt`);
                setText(response.data);
                setIsAudio(false);
            } catch (error) {
                console.error(error);
            }
        };

        const fetchAudio = async () => {
            try {
                const response = await axios.get(`${process.env.PUBLIC_URL}/music.wav`, {
                    responseType: 'blob'
                });
                const blob = new Blob([response.data]);
                const url = URL.createObjectURL(blob);
                setAudioSrc(url);
                setIsAudio(true);
            } catch (error) {
                console.error(error);
            }
        };

        if (props.isAudio) {
            fetchAudio();
        }else {
            fetchText();
        }
    }, [transcriptNumber, props.isAudio]);

    //Submit Button
   
   
  
       
        

        // const pathToPythonFile = '../../../swara_to_music.py';
        
        
            const handleSubmit = () => {
                axios.post('http://localhost:5000/run-script')
                  .then(response => {
                    console.log(response.data);
                  })
                  .catch(error => {
                    console.log(error);
                  });
                 
              };
              
   

    return (
        <>
            <div
                className='container'
                style={{ color: props.mode === 'dark' ? 'white' : '#042743' }}
            >
                <div className='mb-3' style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    {isAudio && (
                        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '1rem', width: '100%', height: '100%' }}>
                            <audio controls src={audioSrc} />
                        </div>
                    )}
                    <h3 className='mb-4'>{props.heading}</h3>
                    <textarea
                        className='form-control'
                        style={{
                            backgroundColor: props.mode === 'dark' ? '#13466e' : 'white',
                            color: props.mode === 'dark' ? 'white' : '#042743',
                        }}
                        id='myBox'
                        rows='4'
                        value={text}
                    />
                </div>
                <div className="d-flex justify-content-center">
                    <button className='btn btn-primary mx-1 my-1' onClick={handleSubmit} style={{ backgroundColor: "limegreen" }}>Submit</button>

                </div>
            </div>
        </>
    );

}
