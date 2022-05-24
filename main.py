import model
from ccxt import binance
import streamlit as st 
import datetime
from PIL import Image

image = Image.open('logo.png')
st.set_page_config(page_title='Wholesale Crypto', page_icon = image, initial_sidebar_state = 'auto')


# st.title("Wholesale Crypto")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)



img = st.sidebar.image(image)

API = st.sidebar.text_input("Enter API Key")
SECRET = st.sidebar.text_input("Enter API Secret")

exchange = binance({
   "apiKey":API, #st.session_state['api_key'],
   "secret": SECRET,#st.session_state['secret'],
   "enableRateLimit": True,
})


Select_menu = st.sidebar.selectbox(
   "Please Select from Menu?",
   ("Buy Trade", "Sell Trade")
)


###########
test_mode = st.sidebar.checkbox("Test Mode: ",value=True)
params = {
   "test": test_mode  # test if it"s valid, but don"t actually place it
         }
##########
reset = st.sidebar.button("Reset wallet",on_click=model.reset_coins)


############
# BUY MODE #
############

if Select_menu == "Buy Trade":
   st.markdown("""<style> span[data-baseweb="tag"] {background-color: white !important; color:black !important;}</style>""", unsafe_allow_html=True,)

   # Choosing coins
   default_coins = []
   empty_lst=[]
   all_symbols = list(set(model.get_all_symbols()))
   special_coins = list(set(model.get_special_coins()))
   sold_coins = list(set(model.get_sold_coins()))

   st.subheader("Buy Trade:")
   selection_mode = st.radio("Select your desired coins:", ('Select All', 'Unselect All', 'Special Coins', 'Frequantly Sold'))

   if selection_mode == 'Select All':
      default_coins = all_symbols
   elif selection_mode == 'Unselect All':
      default_coins = empty_lst
   elif selection_mode == 'Special Coins':
      default_coins = special_coins
   else:
      default_coins = sold_coins
   
   order_coins = st.multiselect(" ",all_symbols,default_coins)
   if selection_mode == 'Special Coins':
      save_special = st.button("save special coins")
      if save_special:
         model.make_special_coins(order_coins, all_symbols)
   st.write(order_coins)
   

   try:
      ccxt_bal= exchange.fetch_balance({'recvWindow': 60000})
      usdt_balance=round(ccxt_bal['USDT']['free'])
   except:
      usdt_balance = "Please Enter your API key & Secret"
   # Balance Info
   usdt_amount = st.number_input("Amount in USDT to trade for each Pair",min_value=0)
   st.text("Balance information:")
   st.caption (f"USDT Balance:  {usdt_balance} ")
   st.caption (f"Number of chosen coins:  {len(order_coins)} ")
   st.caption (f"Estimated Cost of purchase order: {len(order_coins)*usdt_amount}")


   execute = st.button("Execute Orders")

   if(execute):
      model.create_buy_order(usdt_amount, order_coins, params, exchange)




#############
# SELL MODE #
#############

if Select_menu == "Sell Trade":
   st.markdown("""<style> span[data-baseweb="tag"] {background-color: white !important; color:black !important;}</style>""", unsafe_allow_html=True,)

   st.subheader("Sell Trade:")
   def update_prices(lst,exchange):
      for x in lst:
         model.update_price(x['symbol'],exchange)

   coin_list = model.get_wallet_balance()
   print(coin_list)
   col1,col2 =st.columns(2)
   selection_mode = col1.radio("Choose your selection mode:", ('All', 'Winning Coins', 'Losing Coins'))

   if selection_mode == 'All':
      selection_list = coin_list
   elif selection_mode == 'Winning Coins':
      selection_list = [x for x in coin_list if (x['last_price']*x['volume'] - x['costed'])>0]
   else:
      selection_list = [x for x in coin_list if (x['last_price']*x['volume'] - x['costed'])<=0]

   with col2:
      time_def = datetime.timedelta(hours=3)
      nowtime = datetime.datetime.now() + time_def
      formated_time = nowtime.strftime("%H:%M:%S") 
      st.text("last update: "+ formated_time)
      st.button("Update prices", on_click= update_prices(coin_list, exchange))
   
   def modify_list(x):
      if x['last_price']* x['volume'] - x['costed'] > 0:
         label = "🟢  "+ x['symbol'] + "  (+ "  + str(round(x['last_price']*x['volume'] - x['costed'],3))+" )"
      else:
         label = "🔻  "+ x['symbol'] + "  ( "  + str(round(x['last_price']*x['volume'] - x['costed'],3))+" )"
      # label=st.checkbox(label=x['symbol'])
      return label

   order_list = st.multiselect(label=" ",options=selection_list,default=selection_list, format_func=modify_list)

   selling_type = st.radio(
   "Please Select Selling Option.",
   ("USD", "Percentage %"))
   if selling_type == "USD":
      order_amount = st.number_input("amount to sell (in USDT): ", min_value=0)
   else:
      order_amount = st.slider("Percentage to sell: ", min_value=0, max_value=100, value=50, step=10)

   submit_button = st.button(label="Execute Orders")
   if submit_button:
      model.create_sell_order(options_selected= order_list, params= params,exchange=exchange,type= selling_type, sell_amount= order_amount)

#############
# Auto SELL #
# #############

#    if Select_menu == "Auto Sell":
#       st.subheader("Auto Sell:")

#       col1,col2 =st.columns(2)
#       mode= col1.radio("choose your auto sell mode:",("wallet total","single coins"))
#       percentage= col2.slider("Select your Minimum Percentage: ", min_value=0, max_value=20, value=2, step=1)
#       start= col1.button("start the bot")
#       stop= col2.button("stop the bot")


#       total_cost = 0
#       total_profit= 0
#       coin_list = model.get_wallet_balance()
#       for coin in coin_list:
#          cost = coin['costed']
#          profit = coin['last_price']*coin['volume'] - coin['costed']
#          total_cost += cost
#          total_profit += profit
      