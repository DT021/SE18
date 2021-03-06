from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.views.generic.base import TemplateView


urlpatterns = [
	url("badges/", include("pinax.badges.urls", namespace="pinax_badges")),
	path('', views.index, name='index'),
	path('newLeague',views.newLeague,name='newLeague'),
	#path('', TemplateView.as_view(template_name='home.html'), name='home'),
	path('logout_view',views.logout_view,name='logout_view'),
	#path('get_user', views.get_user, name = 'get_user'),
	path('submitSignup', views.submitSignup, name = 'submitSignup'),
	path('submitBuy', views.submitBuy, name = 'submitBuy'),
	path('submitSell', views.submitSell, name = 'submitSell'),
	path('signup', views.signup, name ='signup'),
	path('login', views.login, name='login'),
	#path('submitLogin', views.submitLogin, name = 'submitLogin'),
	path('aboutus', views.aboutus, name='aboutus'),
	path('home', views.home, name='home'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('createleague', views.createleague, name='createleague'),
	path('universal', views.universal, name='universal'),
	path('leagues/<int:league_id>/', views.leagues, name='leagues'),
	path('aipage/<int:league_id>/', views.aipage, name='aipage'),
	path('profile', views.profile, name='profile'),
	path('faq', views.faq, name='faq'),
	path('buypage/<int:league_id>/<int:player_id>/', views.buypage, name='buypage'),
	path('buy/<int:league_id>/<int:player_id>/',views.submitBuy,name='submitBuy'),
	path('sell/<int:league_id>/<int:player_id>/<int:asset_id>/', views.sellform, name='sellform'),
	path('sell2/<int:league_id>/<int:player_id>/<int:asset_id>/', views.submitSell, name='submitSell'),
	path('profile', views.profile, name='profile'),
	path('mission', views.mission, name="mission"),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('accounts/login/', auth_views.LoginView.as_view(template_name='rlogin.html')),
	path('universal', views.universal, name='universal'),
	path('createai', views.createai, name='createai'),
	path('createaipage', views.createaipage, name='createaipage'),
	path('joinLeague', views.joinLeague, name='joinLeague'),
	path('anonuser', views.anonuser, name='anonuser'),
	path('settings', views.settings, name='settings'),

	path('sms/',views.sms, name='sms'),

	path('shop', views.shop, name='shop'),
	path('awards',views.awards, name='awards'),
	path('leaderboard',views.leaderboard, name='leaderboard'),

	path('receipt/<int:transaction_id>/', views.transactionReceipt, name='transactionReceipt'),

	path('submitShop/<int:item>/',views.submitShop, name='submitShop'),

	path('processInvalid', views.processInvalid, name='processInvalid')


	]

