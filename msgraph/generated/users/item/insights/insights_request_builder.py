from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import office_graph_insights
    from ....models.o_data_errors import o_data_error
    from .shared import shared_request_builder
    from .shared.item import shared_insight_item_request_builder
    from .trending import trending_request_builder
    from .trending.item import trending_item_request_builder
    from .used import used_request_builder
    from .used.item import used_insight_item_request_builder

class InsightsRequestBuilder():
    """
    Provides operations to manage the insights property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InsightsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/insights{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[InsightsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property insights for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[InsightsRequestBuilderGetRequestConfiguration] = None) -> Optional[office_graph_insights.OfficeGraphInsights]:
        """
        Get insights from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[office_graph_insights.OfficeGraphInsights]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import office_graph_insights

        return await self.request_adapter.send_async(request_info, office_graph_insights.OfficeGraphInsights, error_mapping)
    
    async def patch(self,body: Optional[office_graph_insights.OfficeGraphInsights] = None, request_configuration: Optional[InsightsRequestBuilderPatchRequestConfiguration] = None) -> Optional[office_graph_insights.OfficeGraphInsights]:
        """
        Update the navigation property insights in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[office_graph_insights.OfficeGraphInsights]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import office_graph_insights

        return await self.request_adapter.send_async(request_info, office_graph_insights.OfficeGraphInsights, error_mapping)
    
    def shared_by_id(self,id: str) -> shared_insight_item_request_builder.SharedInsightItemRequestBuilder:
        """
        Provides operations to manage the shared property of the microsoft.graph.officeGraphInsights entity.
        Args:
            id: Unique identifier of the item
        Returns: shared_insight_item_request_builder.SharedInsightItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .shared.item import shared_insight_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharedInsight%2Did"] = id
        return shared_insight_item_request_builder.SharedInsightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[InsightsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property insights for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[InsightsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get insights from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[office_graph_insights.OfficeGraphInsights] = None, request_configuration: Optional[InsightsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property insights in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def trending_by_id(self,id: str) -> trending_item_request_builder.TrendingItemRequestBuilder:
        """
        Provides operations to manage the trending property of the microsoft.graph.officeGraphInsights entity.
        Args:
            id: Unique identifier of the item
        Returns: trending_item_request_builder.TrendingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .trending.item import trending_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["trending%2Did"] = id
        return trending_item_request_builder.TrendingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def used_by_id(self,id: str) -> used_insight_item_request_builder.UsedInsightItemRequestBuilder:
        """
        Provides operations to manage the used property of the microsoft.graph.officeGraphInsights entity.
        Args:
            id: Unique identifier of the item
        Returns: used_insight_item_request_builder.UsedInsightItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .used.item import used_insight_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["usedInsight%2Did"] = id
        return used_insight_item_request_builder.UsedInsightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def shared(self) -> shared_request_builder.SharedRequestBuilder:
        """
        Provides operations to manage the shared property of the microsoft.graph.officeGraphInsights entity.
        """
        from .shared import shared_request_builder

        return shared_request_builder.SharedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trending(self) -> trending_request_builder.TrendingRequestBuilder:
        """
        Provides operations to manage the trending property of the microsoft.graph.officeGraphInsights entity.
        """
        from .trending import trending_request_builder

        return trending_request_builder.TrendingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def used(self) -> used_request_builder.UsedRequestBuilder:
        """
        Provides operations to manage the used property of the microsoft.graph.officeGraphInsights entity.
        """
        from .used import used_request_builder

        return used_request_builder.UsedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InsightsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class InsightsRequestBuilderGetQueryParameters():
        """
        Get insights from users
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class InsightsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[InsightsRequestBuilder.InsightsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class InsightsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

