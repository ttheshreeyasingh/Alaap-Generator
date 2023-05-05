import { useState, useEffect } from 'react';
import * as React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import TextForm from './TextForm';


const AudioPlayerWithTextForm = () => {
    const [transcriptNumber, setTranscriptNumber] = useState(1);
    const [isAudio, setIsAudio] = useState(false);

    useEffect(() => {
        setIsAudio(false);
    }, [transcriptNumber]);

    useEffect(() => {
        setIsAudio(true);
    }, [transcriptNumber]);
    return (
        <>
          <div className="row">
            <Stack direction="row" spacing={2} justifyContent="center" alignItems="center">
              <h5 style={{ textAlign: 'center' }}>Upload Raaga.json File</h5>
              <Button variant="contained" component="label">
                Upload
                <input hidden accept="application/json" multiple type="file" />
              </Button>
            </Stack>
            <div className="col">
              <TextForm isAudio={isAudio} />
            </div>
          </div>
        </>
      );
      
};

export default AudioPlayerWithTextForm;