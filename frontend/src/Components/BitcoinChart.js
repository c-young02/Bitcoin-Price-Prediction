import React, { useRef, useEffect, useState } from 'react';
import { ColorType, createChart } from 'lightweight-charts';

function BitcoinChart({ chartData }) {
	const chartContainerRef = useRef();
	const [isCandleGraph, setIsCandleGraph] = useState(true);
	const [chart, setChart] = useState(null);

	useEffect(() => {
		const newChart = createChart(chartContainerRef.current, {
			layout: {
				background: { type: ColorType.Solid, color: '#1E1E1E' },
				textColor: 'white',
			},
			grid: {
				vertLines: { color: '#1E1E1E' },
				horzLines: { color: '#1E1E1E' },
			},
			crosshair: {
				vertLine: {
					color: '#00ccff',
					labelBackgroundColor: '#8EA8C3',
				},
				horzLine: {
					color: '#00ccff',
					labelBackgroundColor: '#8EA8C3',
				},
			},
			timeScale: {
				borderColor: '#8EA8C3',
			},
			rightPriceScale: {
				borderColor: '#8EA8C3',
			},
			width: chartContainerRef.current?.clientWidth, // Access clientWidth with optional chaining
			height: 500,
		});
		setChart(newChart);

		const handleResize = () => {
			if (chartContainerRef.current) {
				// Check if chartContainerRef.current is not null
				newChart.applyOptions({
					width: chartContainerRef.current.clientWidth,
				});
			}
		};

		window.addEventListener('resize', handleResize);

		return () => {
			window.removeEventListener('resize', handleResize);
			newChart.remove();
		};
	}, []);

	useEffect(() => {
		if (chart && chartData) {
			const seriesType = isCandleGraph
				? 'addCandlestickSeries'
				: 'addAreaSeries';
			const newSeries = chart[seriesType]();
			newSeries.setData(chartData);
		}
	}, [chart, chartData, isCandleGraph]);

	return (
		<div className="mt-3">
			<div ref={chartContainerRef}></div>
		</div>
	);
}

export default BitcoinChart;
