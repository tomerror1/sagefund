<template lang="html">
  <sui-table :columns="columns">
    <sui-table-header>
      <sui-table-row>
        <sui-table-header-cell  v-for="(item,index) in tableHeaders"
																v-bind:key="index">
					{{item}}
				</sui-table-header-cell>
      </sui-table-row>
    </sui-table-header>
    <sui-table-body>
      <sui-table-row  v-for="(row, index) in rowData" v-bind:key="index">
        <sui-table-cell> {{ row.date }} </sui-table-cell>
        <sui-table-cell> {{ row.asset }} </sui-table-cell>
        <sui-table-cell> {{ row.buySell }} </sui-table-cell>
        <sui-table-cell> {{ row.shares }} </sui-table-cell>
        <sui-table-cell> {{ row.priceAtPurchase }} </sui-table-cell>
				<sui-table-cell> {{ row.transactionFees }} </sui-table-cell>
        <sui-table-cell> {{ row.valueOfTransaction }} </sui-table-cell>
      </sui-table-row>
    </sui-table-body>
  </sui-table>
</template>

<script>
export default {
  name: "TransactionTable",
  data: function() {
    return {
			tableHeaders: ['Date', 'Asset', 'Buy / Sell', 'Shares', 'Price At Purchase', 'Transaction Fees', 'Value of Transaction'],
			rowData: [{
				date: '3rd Nov Sun 2019',
				asset: 'Tesla Stocks',
				buySell: 'Buy',
				shares: '20',
				priceAtPurchase: '13',
				transactionFees: '12',
				valueOfTransaction: '40',
			},
			{
				date: '27th Nov Sat 2019',
				asset: 'SpaceX Stocks',
				buySell: 'Sell',
				shares: '34',
				priceAtPurchase: '2',
				transactionFees: '10',
				valueOfTransaction: '45',
			},
			{
				date: '13th Dec Wed 2019',
				asset: 'Boring Co. Stocks',
				buySell: 'Buy',
				shares: '80',
				priceAtPurchase: '56',
				transactionFees: '78',
				valueOfTransaction: '22',
			}]
		};
	},
	computed: {
		columns: function() {
			return this.tableHeaders.length;
		}
	}
};
</script>
