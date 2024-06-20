from rest_framework import viewsets, status
from rest_framework.response import Response

from cart.entity.cart import Cart
from cart.serializers import CartSerializer
from cart.service.cart_service_impl import CartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


class CartView(viewsets.ViewSet):
    queryset = Cart.objects.all()
    cartService = CartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()



    def cartRegister(self, request):
        try:
            data = request.data

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.cartService.registerCart(data, accountId)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('장바구니 담기 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

