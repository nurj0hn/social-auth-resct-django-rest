import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory } from "react-router-dom";
import { baseBackendUrl } from '../urls';


const TwitchLogin = ({ params, setToken, setMessage }) => {

    // used for redirecting back to homepage after successful login
    const history = useHistory();

    // slices and returns code for backend code submission
    // let accessCode = params.location.pathname.split("&")[1].split("=")[1].replace("%", '/');
    // console.log(accessCode)
    let accessCodee = params.location.pathname;
    console.log(accessCodee)
    // used for POST request parameter in submitCode
    // let codeParams = {
    //     'code': accessCodee
    // }
    window.localStorage.setItem('code', accessCodee)
    let codeParams = window.localStorage.getItem('code')
    console.log(codeParams)

    // make POST request to backend with access code,
    // get back key for auth, store in localStorage.
    const submitCode = async () => {
        setMessage(['Logging in with twitch...']);
        await axios.post(`${baseBackendUrl}/auth/google/connect/`, codeParams).then(res => {
            // console.log('putting token into locaStorage..');
            let token = localStorage.setItem('token', res.data.key);
            // console.log("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG" + res.data.key)
            setToken(token);
            setMessage(['Logged in successfully with Twitch!']);
            history.push('/');
        })
        .catch(err => {
            console.log(err);
            setMessage(['An error occured while connecting to the server.']);
        });
    }

    useEffect(() => {
        submitCode();
    }, []);

    return (
        <>
        </>
    )
}

export default TwitchLogin;