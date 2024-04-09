import React, { useEffect, useState } from 'react';
import Axios from 'axios';
import moment from 'moment';
import BitcoinChart from './BitcoinChart';

function GetData() {
	var timeArray = [];
	var priceArray = [];

	const [bitcoinData, setBitcoinData] = useState([]);
	const [isCandleGraph, setIsCandleGraph] = useState(true);

	var initialData = [];

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
				const data = res.data.Data.Data;
				mapData(data);
				setBitcoinData(initialData);
			})
			.catch((err) => {
				console.log('Error: ' + err);
			});
	}, [setBitcoinData]);

	const mapData = (data) => {
		if (initialData.length === 0) {
			data.forEach((item) => {
				initialData.push({
					time: moment.unix(`${item.time}`).format('YYYY-MM-DD'),
					open: item.open,
					high: item.high,
					low: item.low,
					close: item.close,
				});
			});
		}
	};

	return (
		<div className="">
			<BitcoinChart chartData={bitcoinData} isCandleGraph={isCandleGraph} />
		</div>
	);
}

export default GetData;
