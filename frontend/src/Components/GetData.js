import { useEffect, useState } from 'react';
import Axios from 'axios';
import moment from 'moment';
import BitcoinChart from './BitcoinChart';

function GetData() {
	var timeArray = [];
	var priceArray = [];

	const [bitcoinData, setBitcoinData] = useState([]);

	var initialData = [];

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

				console.log(initialData);

				setBitcoinData(initialData);
			})
			.catch((err) => {
				console.log('Error: ' + err);
			});
	}, [setBitcoinData]);

	const mapData = (data) => {
		if (initialData.length === 0) {
			data.forEach((data) => {
				priceArray.push(data.close);
				timeArray.push(moment.unix(`${data.time}`).format('YYYY-MM-DD'));
				initialData.push({
					time: moment.unix(`${data.time}`).format('YYYY-MM-DD'),
					value: data.close,
				});
			});
		}
	};

	return (
		<div className="">
			<BitcoinChart ChartData={bitcoinData} />
		</div>
	);
}

export default GetData;
