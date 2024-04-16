import { useRef, useEffect, useState } from 'react';
import { ColorType, createChart } from 'lightweight-charts';

function BitcoinChart(LineData) {
	const chartContainerRef = useRef();

	useEffect(() => {
		var d = LineData;

		const chart = createChart(chartContainerRef.current, {
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

			width: chartContainerRef.current.clientWidth,
			height: 500,
		});

		const newSeries = chart.addAreaSeries({
			lineColor: '#2962FF',
			topColor: '#2962FF',
			bottomColor: 'rgba(41, 98, 255, 0.28)',
		});

		const handleResize = () => {
			chart.applyOptions({
				width: chartContainerRef.current.clientWidth,
			});
		};

		window.addEventListener('resize', handleResize);

		if (LineData.LineData !== undefined) newSeries.setData(LineData.LineData);

		return () => {
			chart.remove();
			window.removeEventListener('resize', handleResize);
		};
	}, [LineData]);

	return (
		<div className="mt-3">
			<div ref={chartContainerRef}></div>
		</div>
	);
}

export default BitcoinChart;
