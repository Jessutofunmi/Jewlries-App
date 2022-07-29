import streamlit as st

def buy():
    st.success("You've Succesfully bought item")
    st.snow()

#engagement rings
def engagement_rings():
    st.header("Engagement Rings")
    st.subheader("The Twig")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/4Q-ER-R-YG_0_cdaac161-443e-4fa7-8cf4-4d962dae39f1_300x.jpg?v=1654597278")
    st.text("$950")
    st.button('Buy', key='btn-1', on_click=buy)
    st.subheader("The Nelly")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/162Q-ER-OV-WG_0_6c562cfa-ef23-48c8-b408-f0706d91df06_700x.jpg?v=1633000142")
    st.text("$950")
    st.button('Buy', key='btn-2', on_click=buy)
    st.subheader("The Kamelie")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/189Q-ER-PR-RG_0_700x.jpg?v=1645618136")
    st.text("$950")
    st.button('Buy', key='btn-3', on_click=buy)
#wedding bands
def wedding_bands():
    st.header("Wedding Bands")
    st.subheader("4mm Twig Cigar") 
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/235Q-WB-R-R02-WG_0_300x.jpg?v=1647167289")
    st.text("$700")
    st.button('Buy', on_click=buy)
    st.subheader("The Natalie")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/2Q-ER-R01-YG_0_700x.jpg?v=1612353488")
    st.text("$400")
    st.button('Buy', key='btn-3', on_click=buy)
    st.subheader("Textured Eternity Twig")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/226QT-WB-RG-LDIAM-14_700x.jpg?v=1641992283")
#pendants
def pendants():
    st.header("Pendants")
    st.subheader("The Aubrey")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/252Q-DP-R-YG_06_300x.jpg?v=1645611899")
    st.text("$700")
    st.button('Buy', on_click=buy) 
    st.subheader("The Billie")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/249Q-DP-R-WG_06_700x.jpg?v=1645610768")
    st.text("$1,050")
    st.button('Buy', key='btn-2', on_click=buy)
    st.subheader("The Amelia")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/243Q-DP-R-RG_06_900x.jpg?v=1645609409")
    st.text("$600")
    st.button('Buy', key='btn-3', on_click=buy)

#eternity rings
def eternity_ring():
    st.header("Eternity Rings")
    st.subheader("The Danielle Round Eternity")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/177Q-ET-R-3_0-YG_0_60dfff1b-b3a7-4215-a4e3-1bc5f59bde92_700x.jpg?v=1645108813")
    st.text("$2,250")
    st.button('Buy', on_click=buy)
    st.subheader("The Elianne Round Eternity")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/178Q-ET-R-3_0-WG_0_bcf49446-c42e-4444-8a70-66a0ccec4f93_700x.jpg?v=1646152121")
    st.text("$2,520")
    st.button('Buy', key='btn-2', on_click=buy)
    st.subheader("The Jessica Emerald Eternity")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/171Q-ET-EM-2x3_05-RG_0_1f1363db-9428-4461-9090-577e59be178e_700x.jpg?v=1645015709")
    st.text("$4,500")
    st.button('Buy', key='btn-3', on_click=buy)
#diamond necklaces
def diamond_necklaces():
    st.header("Diamond Necklaces")
    st.subheader("Initial Diamond Pendant")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/257Q-FP-A-YG_06_50c7acd9-d761-49b7-9c55-d0245f9662f9_700x.jpg?v=1648374088")
    st.text("$663")
    st.button('Buy', on_click=buy)
    st.subheader("Diamond Zodiac Pendant")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/254Q-FP-Aquarius-WG_06_700x.jpg?v=1648021955")
    st.text("$723")
    st.button('Buy', key='btn-2', on_click=buy)
    st.subheader("Diamond X Pendant")
    st.image("https://cdn.shopify.com/s/files/1/0039/6994/1568/products/269Q-FP-RG_06_bba9b302-c90c-43b1-b5e3-66d4b5c67746_700x.jpg?v=1648534588")
    st.text("$1,275")
    st.button('Buy', key='btn-3', on_click=buy)
#clothing
def clothing():
    st.header("Clothing")
    st.subheader("Men's African Dashiki Shirt Long Sleeve Luxury Metallic Gold Totem Printed Traditional Vintage Shirts Tuxedo Shirts")
    st.image("https://litb-cgis.rightinthebox.com/images/640x640/202203/bps/product/inc/wrpajd1646189649040.jpg?fmt=webp&v=1")
    st.text("$27.99")
    st.button('Buy', on_click=buy)
    st.subheader("SHENBOLEN Women African Print Dresses Autumn and Winter Long Sleeves Ankara Dress")
    st.image("https://m.media-amazon.com/images/I/81PR6Nk4V6L._AC_UY550_.jpg")
    st.text("$38.88")
    st.button('Buy', key='btn-2', on_click=buy)
    st.subheader("African Kids Clothes, Ankara Kids Clothes, Boys African Attire, Eid Outfit, African Birthday Outfit, Wedding Outfit and Special Event")
    st.image("https://i.etsystatic.com/28530272/r/il/fd142f/3730615612/il_794xN.3730615612_ijeu.jpg")
    st.text("$69.99")
    st.button('Buy', key='btn-3', on_click=buy)
    st.subheader("YOUNGER TREE African Baby Clothes Girl Dashiki Ankara Outfit Set")
    st.image("https://m.media-amazon.com/images/I/71e1qAwDbYL._AC_UX569_.jpg")
    st.text("$18.99")
    st.button('Buy', key='btn-4', on_click=buy)



#navigation bar
navigation = st.sidebar.selectbox('Jelwries and Clothing', ["Engagement Rings", "Wedding Bands", "Pendants", "Eternity Rings", "Diamond Necklaces", "Clothing"])

st.title("Shukurat's Clothing and Jelwries Store")
st.image("https://www.hudsonpoole.com/blog/wp-content/uploads/2018/08/hudsonpoole-pendant-banner.jpg")





if navigation == "Engagement Rings":
    engagement_rings()
elif navigation == "Wedding Bands":
    wedding_bands()
elif navigation == "Pendants":
    pendants()
elif navigation == "Eternity Rings":
    eternity_ring()
elif navigation == "Diamond Necklaces":
    diamond_necklaces()
elif navigation == "Clothing":
    clothing()