import { useEffect, useState } from 'react';
import Axios from 'axios';
import '../config.js';

export default function CryptoInfo() {
	const [cryptoInfo, setCryptoInfo] = useState([]);

	useEffect(() => {
		Axios({
			method: 'get',
			url: `http://${global.config.localhost}:5000/CryptoInfo`,
		})
			.then((res) => {
				// console.log(res.data);
				setCryptoInfo(res.data);
			})
			.catch((err) => {
				console.log('Error: ' + err);
			});
	}, []);

	return (
		<div className="w-100">
			{console.log(cryptoInfo.circulating_supply)}
			<div className="border-bottom border-white p-1">
				<h3 className="text-white text-center">Bitcoin</h3>
			</div>
			<table className="w-100">
				<tbody className="text-center">
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Market Rank:
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.rank}`}</h4>
						</td>
					</tr>
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Predicted Price
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.predicted_price}`}</h4>
						</td>
					</tr>
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Current Price
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.current_price}`}</h4>
						</td>
					</tr>
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Market Cap:
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.market_cap}`}</h4>
						</td>
					</tr>
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Market Dominance:
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.market_dominance}`}</h4>
						</td>
					</tr>
					<tr>
						<th className="w-50 border border-white border-bottom-0 border-top-0 text-center">
							<h4 className="text-white p-2 border-right border-white">
								Circulating Supply:
							</h4>
						</th>
						<td className="w-50 border border-white border-bottom-0 border-top-0">
							<h4 className="text-white p-2 border-left">{`${cryptoInfo.circulating_supply}`}</h4>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	);
}
