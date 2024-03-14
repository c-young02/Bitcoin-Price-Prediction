import ReactSpeedometer from "react-d3-speedometer"
import { useEffect, useState } from "react"
import Axios from "axios"


export default function Speedometer(){

    const [currentValue, setCurrentValue] = useState(0);

    useEffect(() => {

        Axios({
            method: "get",
            url: "http://127.0.0.1:5000/FearandGreed",

        }).then((res) => {

            console.log(res.data);
            setCurrentValue(res.data);



        }).catch((err) => {
            console.log("Error: "+err);
        }); 

    }, [])




    // const mapData = (data) => {

    //     if (initialData.length === 0){
    //         data.forEach(data => {

    //             priceArray.push(data.close);
    //             timeArray.push(moment.unix(`${data.time}`).format("YYYY-MM-DD"));
    //             initialData.push({time: moment.unix(`${data.time}`).format("YYYY-MM-DD"), value: data.close});
              
    //         });
    //     }
    // }



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