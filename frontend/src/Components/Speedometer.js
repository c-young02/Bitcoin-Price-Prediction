import ReactSpeedometer from "react-d3-speedometer";
import { useEffect, useState } from "react";
import Axios from "axios";
import '../config.js';


export default function Speedometer(){

    const [currentValue, setCurrentValue] = useState(0);

    useEffect(() => {

        Axios({
            method: "get",
            url: `http://${global.config.localhost}:5000/FearandGreed`,

        }).then((res) => {

            console.log(res.data);
            setCurrentValue(res.data);



        }).catch((err) => {
            console.log("Error: "+err);
        }); 

    }, [])

    return (
        <div style={{
            width: "500px",
            height: "300px"}}
            >
            <ReactSpeedometer
                fluidWidth={true}
                value={currentValue * 10}
                currentValueText="Happiness Level"
                customSegmentLabels={[
                {
                    text: "Extreme Fear",
                    position: "INSIDE",
                    color: "#555",
                },
                {
                    text: "Fear",
                    position: "INSIDE",
                    color: "#555",
                },
                {
                    text: "Neutral",
                    position: "INSIDE",
                    color: "#555",
                    fontSize: "19px",
                },
                {
                    text: "Greed",
                    position: "INSIDE",
                    color: "#555",
                },
                {
                    text: "Extreme Greed",
                    position: "INSIDE",
                    color: "#555",
                },
                ]}
            />

            {console.log("this is the current value " + currentValue)}
        </div>
    )
}