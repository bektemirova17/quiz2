import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {ProviderService} from './shared/services/provider.service';

import {HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [

    
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    ProviderService
  ],
  bootstrap: []
})
export class AppModule { }