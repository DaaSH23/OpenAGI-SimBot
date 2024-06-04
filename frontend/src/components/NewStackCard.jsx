import React, { useContext } from 'react';
import '../App.css';
import NewStackFormPop from './NewStackFormPop';
import { AppContext } from '../utils/AppContext';

const CardComponent = () => {
    const { open, setOpen } = useContext(AppContext);
    return (
        <>
            <div className="card-container">
                <div className="card">
                    <h1 className='cardTitle'>Create New Stack</h1>
                    <p className='subHeadcard'>Start building your generative AI apps with our essential tools and frameworks</p>
                    <button className="newStackButton mt-4" onClick={() => setOpen(true)}><span className="plusIcon">+</span> New Stack</button>
                </div>
            </div>
            <NewStackFormPop/>
        </>
    );
};

export default CardComponent;