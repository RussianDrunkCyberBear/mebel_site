from django.shortcuts import render
from .models import PortfolioItem, PortfolioImage

# Create your views here.

def portfolio_cat(request):
	# portfolios_images = PortfolioImage.objects.filter(is_main=True, is_active=True)
	portfolios = PortfolioItem.objects.filter(is_active=True)
	return render(request, 'portfolio/portfolio_cat.html', locals())

def portfolio_card(request, portfolio_id):
	portfolio_item = PortfolioItem.objects.get(id=portfolio_id)
	# portfolio_main_image = PortfolioImage.objects.get(prfol_product=portfolio_item, is_active=True, is_main=True)
	portfolio_main_image = portfolio_item.main_image.image
	portfolio_images = PortfolioImage.objects.filter(prfol_product=portfolio_item, is_active=True).exclude(id=portfolio_item.main_image.id)
	return render(request, 'portfolio/portfolio_card.html', locals())