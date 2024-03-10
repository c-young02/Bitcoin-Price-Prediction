import {useRef, useEffect, useState} from 'react'
import { ColorType, createChart } from 'lightweight-charts';

function BitcoinChart(ChartData) {

    const chartContainerRef = useRef();



    useEffect(() => {

        var d = ChartData;

        console.log(ChartData.ChartData);
        

        console.log("This is bitoin data "+ ChartData)

        const chart = createChart(chartContainerRef.current, {
            layout:{
                background: {type: ColorType.Solid, color: "white"}
            },

            // width: chartContainerRef.current.clientWidth,
            // height: 200,

            
            width: chartContainerRef.current.clientWidth,
            height: 400,
        });

        const newSeries = chart.addAreaSeries({
            lineColor: "#2962FF",
            topColor: "#2962FF",
            bottomColor: "rgba(41, 98, 255, 0.28)",
        });
        

        if(ChartData.ChartData !== undefined) newSeries.setData(ChartData.ChartData);

        return () => {
            chart.remove();
        }

    }, [ChartData])

    return (
        <div>
            <div ref={chartContainerRef}>

            </div>
            <div>
                Hello
            </div>
        </div>
    );
}

export default BitcoinChart;
