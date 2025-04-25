from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard_view(request):
    servers = Server.objects.all()
    alerts = Alerts.objects.all()
    alert_counts = {
        'critical' : alerts.filter(level = 'critical').count(),
        'medium' : alerts.filter(level = 'filter').count(),
        'low'  : alerts.filter(level = "low").count(),
    }

    usage_stats = UsageStats.objects.all()
    network_traffic = NetworkTraffic.objects.order_by('timestamp')

    context = {
        'servers': servers,
        'alerts': alert_counts,
        'usage_stats': usage_stats,
        'network_traffic' : network_traffic,
    }

    return render (request,'dashboard.html', context)
