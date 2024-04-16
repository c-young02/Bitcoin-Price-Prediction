import { useEffect, useState } from 'react';
import Axios from 'axios';
import moment from 'moment';
import BitcoinChart from './BitcoinChart';
import CandleStick from './CandleStick';

function GetData(isLineGraph) {
	const [lineData, setLineData] = useState([]);
	const [candleData, setCandleData] = useState([]);

	var initialLineData = [];
	var initialCandleData = [];

	var data = [];

	useEffect(() => {
		Axios({
			method: 'get',
			url: `https://min-api.cryptocompare.com/data/v2/histoday?`,
			params: {
				fsym: 'BTC',
				tsym: 'GBP',
				limit: 1500,
			},
		})
			.then((res) => {
				data = res.data.Data.Data;
				mapData(data);

				setLineData(initialLineData);
				setCandleData(initialCandleData);
			})
			.catch((err) => {
				console.log('Error: ' + err);
			});
	}, [setLineData]);

	const mapData = (data) => {
		if (initialLineData.length === 0) {
			data.forEach((data) => {
				initialLineData.push({
					time: moment.unix(`${data.time}`).format('YYYY-MM-DD'),
					value: data.close,
				});
			});
		}

		if (initialCandleData.length === 0) {
			data.forEach((data) => {
				initialCandleData.push({
					time: moment.unix(`${data.time}`).format('YYYY-MM-DD'),
					open: data.open,
					close: data.close,
					low: data.low,
					high: data.high,
				});
			});
		}
	};

	return (
		<div className="">
			{isLineGraph.isLineGraph === true ? (
				<BitcoinChart LineData={lineData} />
			) : (
				<CandleStick CandleData={candleData} />
			)}
		</div>
	);
}

export default GetData;
