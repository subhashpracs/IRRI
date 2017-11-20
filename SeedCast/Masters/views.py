from django.core.serializers import json
from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import request, Http404
from .models import Dealer_Registration, AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, DealerDemand, Feedback, States, Districts, Blocks, Panchayats, Villages, Stock, VAWDemand, SPO, Vawmobnum, Varietynew, ViewDealerlist, Pilotplots
from .serializers import DealerSerializer, AAOSerializer, VAWSerializer, STRVCategorySerializer, STRVVarietySerializer, MobnumSerializer, DealerDemandSerializer, FeedbackSerializer, StatesSerializer, DistrictsSerializer, BlocksSerializer, PanchayatsSerializer, VillagesSerializer, StockSerializer, VAWDemandSerializer, SPOSerializer, VAWMobSerializer, VarietynewSerializer, ViewDealerSerializer, PilotPlotsSerializer
from rest_framework import generics
from highcharts.views import HighChartsBarView
from highcharts.views import HighChartsPieView
from rest_framework import status

#Cairo charts...


import pycha.bar
import cairo

class Example(APIView):

    width, height = (500, 400)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)



    dataSet = (
      ('dataSet 1', ((0, 1), (1, 3), (2, 2.5))),
      ('dataSet 2', ((0, 2), (1, 4), (2, 3))),
      ('dataSet 3', ((0, 5), (1, 1), (2, 0.5))),
    )


    options = {
        'legend': {'hide': True},
        'background': {'color': '#f0f0f0'},
    }

    chart = pycha.bar.VerticalBarChart(surface, options)
    chart.addDataset(dataSet)
    #chart.render()



    surface.write_to_png('output.png')



#Dealer's list
class DealerList(APIView):
    def get(self, request, format=None):
        dealer = Dealer_Registration.objects.all()
        serializer = DealerSerializer(dealer, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DealerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealerDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Dealer_Registration.objects.get(pk=pk)
        except Dealer_Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dealer = self.get_object(pk)
        dealer = DealerSerializer(dealer)
        return Response(dealer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = DealerSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#AAO Registration Model view
class AAOList(generics.ListCreateAPIView):
    queryset = AAO_Registration.objects.all()
    serializer_class = AAOSerializer

class AAODetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AAO_Registration.objects.all()
    serializer_class = AAOSerializer


#VAW Registration Model View
class VAWList(generics.ListCreateAPIView):
    queryset = VAW_Registration.objects.all()
    serializer_class = VAWSerializer

class VAWDetail(APIView):
    def get_object(self, pk):
        try:
            return VAW_Registration.objects.get(pk=pk)
        except VAW_Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vaw = self.get_object(pk)
        vaw = VAWSerializer(vaw)
        return Response(vaw.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = VAWSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#STRV Category
class STRVCategoryList(APIView):

    def get(self, request, format=None):
        category = STRVCategory.objects.all()
        serializer = STRVCategorySerializer(category, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = STRVCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class STRVCategoryDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return STRVCategory.objects.get(pk=pk)
        except STRVCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        category = STRVCategorySerializer(category)
        return Response(category.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = STRVCategorySerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#STRV Variety Model view
class STRVVarietyList(APIView):

    ser = STRVVarietySerializer

    # def get_queryset(self):
    #     category_name = self.kwargs['category_name']
    #     return STRVVariety.objects.filter(category_name=category_name)

    def get(self, request, format=None):
        variety = STRVVariety.objects.all()
        serializer = STRVVarietySerializer(variety, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = STRVVarietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#STRVVariety list as category under...
class STRVVarietyNew(APIView):
    # def get(self,request):
    #     category_name = STRVCategory.objects.all()
    #     variety = STRVVariety.objects.filter(category_name=category_name)
    #     serializer_class = STRVVarietySerializer(variety, many=True)
    #     return Response(serializer_class.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VarietynewSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer:" + str(serializer.data))
            posted_category = serializer.data['category']
            queryset = STRVVariety.objects.filter(category_name=posted_category)
            variety_list = []
            for obj in queryset:
                variety = obj.variety_name
                varietycode = obj.variety_code
                descriptionn = obj.description
                duration = obj.duration_in_days
                land = obj.suitable_land_type
                height = obj.plant_height
                grain = obj.grain_type
                yieldin = obj.yield_in_tonne
                advantage = obj.yield_advantage
                category = obj.category_name
                variety_dic = { "variety_name" : variety, "variety_code" : varietycode, "description" : descriptionn, "duration_in_days" : duration, "suitable_land_type" : land, "plant_height" : height, "grain_type" : grain, "yield_in_tonne" : yieldin, "yield_advantage" : advantage }
                variety_list.append(variety_dic,)

            print("Variety List:" + str(variety_list))
            return Response(variety_list, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class STRVVarietyDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return STRVVariety.objects.get(pk=pk)
        except STRVVariety.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        category = STRVVarietySerializer(category)
        return Response(category.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = STRVVarietySerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Mobile numbers model
class MobnumList(APIView):

    # def get(self, request, format=None):
    #     mob = Mobnum.objects.all()
    #     serializer = MobnumSerializer(mob, many=True)
    #     return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = MobnumSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            mob_posted = serializer.data['mobnum']
            queryset = Dealer_Registration.objects.all()
            dealers = []
            mobile_numbers_list = []
            for obj in queryset:
                mob_num = obj.contact_num
                mobile_numbers_list.append(mob_num)
                #dealer_list = { "dealer_name" : obj.dealer_name, "license" : obj.license_num, "contact" : obj.contact_num, "block" : obj.block_name }
                dealer_list = { "id" : obj.id }
                dealers.append(dealer_list,)

            if mob_posted in mobile_numbers_list:
                mob_index = mobile_numbers_list.index(mob_posted)
                print("Mobile number matched...")
                return Response(dealers[mob_index], status=status.HTTP_200_OK)
            else:
                print("Mobile number not found...")
                no_dealer_data = { "error_msg" : "Not registered...", }
                return Response(no_dealer_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ViewDealer(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        serializer = ViewDealerSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['district']
            queryset = Dealer_Registration.objects.filter(dist_name=dist_posted)
            dealer_dist_wise = []
            for obj in queryset:
                dealer_list = { "dealer_name" : obj.dealer_name, "contact" : obj.contact_num }
                dealer_dist_wise.append(dealer_list,)

            return Response(dealer_dist_wise, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Plots(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        serializer = PilotPlotsSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['dist_name']
            block_posted = serializer.data['block_name']
            #panchayat_posted = serializer.data['panchayat_name']
            queryset = Dealer_Registration.objects.filter(dist_name=dist_posted,block_name=block_posted)
            dealer_list_dbp_wise = []
            for obj in queryset:
                dealer_list = { "shop" : obj.shop_name, "dealer" : obj.dealer_name }
                dealer_list_dbp_wise.append(dealer_list,)

            print("Dealer List:" + str(dealer_list_dbp_wise))

            return Response(dealer_list_dbp_wise, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#VAW Mobile numbers...
class VAWMobileList(APIView):

    # def get(self, request, format=None):
    #     mob = Mobnum.objects.all()
    #     serializer = MobnumSerializer(mob, many=True)
    #     return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = VAWMobSerializer(data=request.data)
        if serializer.is_valid():
            mob_posted = serializer.data['vaw_num']
            queryset = VAW_Registration.objects.all()
            vaws = []
            mobile_numbers_list = []
            for obj in queryset:
                mob_num = obj.VAW_contact_number
                mobile_numbers_list.append(mob_num)
                vaw_list = { "id" : obj.id }
                vaws.append(vaw_list, )

            if mob_posted in mobile_numbers_list:
                mob_index = mobile_numbers_list.index(mob_posted)
                print("Mobile number matched...")
                return Response(vaws[mob_index], status=status.HTTP_200_OK)
            else:
                print("Mobile number not found...")
                no_vaw_data = { "error_message" : "No VAW for this number..." }
                return Response(no_vaw_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Chart View example...
class BarView(HighChartsBarView):
    categories = ['Orange', 'Bananas', 'Apples']

    # @property
    # def title(self):
    #     return 'This is a new Title for graphsview...'
    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []
            for x in range(len(self.categories)):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return render(request, 'graphs.html', context=result)

        # return result

#Dealer Demand model
class DealerDemandList(APIView):

    def get(self, request, format=None):
        demand = DealerDemand.objects.all()
        serializer = DealerDemandSerializer(demand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DealerDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Stock available POST url
class StockList(APIView):

    def get(self, request, format=None):
        demand = Stock.objects.all()
        serializer = StockSerializer(demand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Feedback post url
class FeedbackList(APIView):
    # def get(self, request, format=None):
    #     feedback = Feedback.objects.all()
    #     serializer = FeedbackSerializer(feedback, many=True)
    #     return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatesList(APIView):

    def get(self, request, format=None):
        state = States.objects.all()
        serializer = StatesSerializer(state, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StatesSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictsList(APIView):

    def get(self, request, format=None):
        dist = Districts.objects.all()
        serializer = DistrictsSerializer(dist, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DistrictsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlocksList(APIView):

    def get(self, request, format=None):
        blocks = Blocks.objects.all()
        serializer = BlocksSerializer(blocks, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = BlocksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PanchayatsList(APIView):

    def get(self, request, format=None):
        panchayats = Panchayats.objects.all()
        serializer = PanchayatsSerializer(panchayats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = PanchayatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VillagesList(APIView):

    def get(self, request, format=None):
        villages = Villages.objects.all()
        serializer = VillagesSerializer(villages, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VillagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#SPOs
class SPOList(generics.ListCreateAPIView):
    queryset = SPO.objects.all()
    serializer_class = SPOSerializer


class VAWDemandList(APIView):

    def get(self, request, format=None):
        vawdemand = VAWDemand.objects.all()
        serializer = VAWDemandSerializer(vawdemand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VAWDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
